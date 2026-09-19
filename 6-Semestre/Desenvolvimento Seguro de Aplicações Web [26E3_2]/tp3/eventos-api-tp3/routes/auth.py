from fastapi import APIRouter, HTTPException, Depends, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlmodel import Session

from database.db import get_session, obter_usuario, criar_usuario
from models.usuario import Usuario, UsuarioCreate, TokenResponse, TokenMFAResponse
from auth.security import hash_password, verify_password, criar_token, decodificar_token, SCOPES_POR_PAPEL
from middleware.rate_limit import limiter

router = APIRouter(prefix="/auth", tags=["auth"])


# ── Registro ──────────────────────────────────────────────────────────────────

@router.post("/registrar", status_code=201, response_model=dict)
@limiter.limit("10/minute")   # limite mais relaxado para registro
def registrar(request: Request, dados: UsuarioCreate, session: Session = Depends(get_session)):
    if obter_usuario(session, dados.username):
        raise HTTPException(status_code=400, detail="Username já existe")
    usuario = Usuario(
        username=dados.username,
        hashed_password=hash_password(dados.password),
        papel=dados.papel,
        mfa_habilitado=(dados.papel == "admin"),
    )
    criar_usuario(session, usuario)
    return {"mensagem": f"Usuário '{dados.username}' criado com papel '{dados.papel}'"}


# ── Login com rate limiting restritivo (Ex 7) ─────────────────────────────────

@router.post("/login", response_model=TokenMFAResponse)
@limiter.limit("5/minute")   # Ex 7 — limite mais restritivo que rotas de listagem
def login(
    request: Request,
    form: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    """
    Exercício 7 — rate limiting diferenciado.
    Login: 5 req/min por IP — protege contra força bruta.
    Rotas de listagem: 60 req/min (configurado no main.py).

    Justificativa: um usuário legítimo raramente faz mais de 1-2 logins por minuto;
    um atacante tentando força bruta precisaria de centenas ou milhares de tentativas.
    Limitar apenas o login protege sem prejudicar usuários normais nas rotas de leitura.
    """
    usuario = obter_usuario(session, form.username)
    if not usuario or not verify_password(form.password, usuario.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    escopos = SCOPES_POR_PAPEL.get(usuario.papel, [])

    if usuario.papel == "admin" and usuario.mfa_habilitado:
        token = criar_token(
            sub=usuario.username,
            papel=usuario.papel,
            escopos=["eventos:read"],
            extra_claims={"mfa_pendente": True},
        )
        return TokenMFAResponse(access_token=token, mfa_pendente=True)

    token = criar_token(sub=usuario.username, papel=usuario.papel, escopos=escopos)
    return TokenMFAResponse(access_token=token, mfa_pendente=False)


# ── MFA (simulado) ────────────────────────────────────────────────────────────

class MFAVerify(BaseModel):
    token_parcial: str
    codigo_mfa: str

    class Config:
        extra = "forbid"


@router.post("/mfa/verificar", response_model=TokenResponse)
def verificar_mfa(dados: MFAVerify, session: Session = Depends(get_session)):
    try:
        payload = decodificar_token(dados.token_parcial)
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido")

    if not payload.get("mfa_pendente"):
        raise HTTPException(status_code=400, detail="MFA não está pendente para este token")

    if dados.codigo_mfa != "123456":
        raise HTTPException(status_code=401, detail="Código MFA inválido")

    username = payload["sub"]
    usuario = obter_usuario(session, username)
    escopos = SCOPES_POR_PAPEL.get(usuario.papel, [])
    token = criar_token(sub=username, papel=usuario.papel, escopos=escopos,
                        extra_claims={"mfa_verificado": True})
    return TokenResponse(access_token=token)


# ── M2M ───────────────────────────────────────────────────────────────────────

class M2MCredentials(BaseModel):
    client_id: str
    client_secret: str
    scope: str = "m2m:read"

    class Config:
        extra = "forbid"


@router.post("/m2m/token", response_model=TokenResponse)
def token_m2m(creds: M2MCredentials):
    PARCEIROS = {"parceiro-externo": "secret-parceiro-xpto-2025"}
    if PARCEIROS.get(creds.client_id) != creds.client_secret:
        raise HTTPException(status_code=401, detail="Credenciais M2M inválidas")

    escopos_permitidos = {"m2m:read", "m2m:write"}
    escopos_concedidos = list(set(creds.scope.split()) & escopos_permitidos)
    if not escopos_concedidos:
        raise HTTPException(status_code=400, detail="Escopo não permitido para M2M")

    token = criar_token(sub=creds.client_id, papel="m2m_parceiro", escopos=escopos_concedidos,
                        expire_minutes=60,
                        extra_claims={"client_id": creds.client_id, "grant_type": "client_credentials"})
    return TokenResponse(access_token=token)
