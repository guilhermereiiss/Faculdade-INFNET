from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Request, status, Header
from sqlmodel import Session
from config import settings
from database.db import get_session, obter_usuario_por_username
from models.usuario import LoginRequest, M2MTokenRequest, Token
from auth.security import verify_password, criar_token, SCOPES_POR_PAPEL
from middleware.rate_limit import limiter

router = APIRouter(prefix="/auth", tags=["Autenticação & M2M"])


@router.post(
    "/login",
    response_model=Token,
    summary="Login de usuários com Rate Limiting e MFA para contas administrativas",
)
@limiter.limit("5/minute")
def login(
    request: Request,
    dados: LoginRequest,
    session: Session = Depends(get_session),
    x_mfa_code: Optional[str] = Header(default=None, alias="X-MFA-Code"),
) -> Token:
    """
    Exercício 6 e 10 — Autenticação OAuth2 / JWT:
    - Rate Limiting estrito (5 requisições por minuto por IP) para mitigar força bruta e credential stuffing.
    - Hashing seguro via Bcrypt para validação de senha.
    - MFA simulado: contas com papel 'admin' exigem obrigatoriamente código TOTP de 6 dígitos.
    - Emite JWT com expiração e escopos restritos ao papel do usuário.
    """
    usuario = obter_usuario_por_username(session, dados.username)

    # Prevenção de Enumeração de Usuários (tempo constante de verificação)
    if not usuario or not verify_password(dados.password, usuario.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas. Verifique usuário e senha.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not usuario.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Conta inativa ou bloqueada por segurança.",
        )

    mfa_verified = False
    # Verificação de MFA para Administradores (Exercício 6)
    if usuario.papel == "admin":
        codigo_informado = dados.mfa_code or x_mfa_code
        if not codigo_informado:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Código MFA obrigatório para login de administrador.",
                headers={"WWW-Authenticate": "Bearer error=\"mfa_required\""},
            )
        if codigo_informado != settings.admin_mfa_default_totp:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Código MFA inválido ou expirado.",
                headers={"WWW-Authenticate": "Bearer error=\"invalid_mfa\""},
            )
        mfa_verified = True

    escopos = SCOPES_POR_PAPEL.get(usuario.papel, [])
    token_jwt = criar_token(
        sub=usuario.username,
        papel=usuario.papel,
        escopos=escopos,
        crm=usuario.crm,
        mfa_verified=mfa_verified,
        expire_minutes=settings.access_token_expire_minutes,
    )

    return Token(
        access_token=token_jwt,
        token_type="bearer",
        expires_in=settings.access_token_expire_minutes * 60,
        scope=" ".join(escopos),
        papel=usuario.papel,
        mfa_verified=mfa_verified,
    )


@router.post(
    "/m2m/token",
    response_model=Token,
    summary="Emissão de Token M2M (Client Credentials) para laboratório parceiro",
)
@limiter.limit("20/minute")
def m2m_token(
    request: Request,
    dados: M2MTokenRequest,
) -> Token:
    """
    Exercício 7 — Integração Máquina-a-Máquina (M2M):
    Utiliza fluxo OAuth 2.0 Client Credentials Grant.
    Emite token com claims e escopos específicos ('laboratorio:disponibilidade', 'laboratorio:exames'),
    sem conceder acesso a rotas clínicas de pacientes ou prontuários.
    """
    if (
        dados.client_id != settings.m2m_client_id
        or dados.client_secret != settings.m2m_client_secret
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais de cliente M2M inválidas.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    escopos_m2m = SCOPES_POR_PAPEL.get("m2m_laboratorio", [])
    token_jwt = criar_token(
        sub="m2m:laboratorio",
        papel="m2m_laboratorio",
        escopos=escopos_m2m,
        expire_minutes=60,  # Token de serviço com expiração controlada
        extra_claims={
            "client_id": dados.client_id,
            "tipo_integracao": "laboratorio_parceiro",
        },
    )

    return Token(
        access_token=token_jwt,
        token_type="bearer",
        expires_in=3600,
        scope=" ".join(escopos_m2m),
        papel="m2m_laboratorio",
        mfa_verified=True,
    )
