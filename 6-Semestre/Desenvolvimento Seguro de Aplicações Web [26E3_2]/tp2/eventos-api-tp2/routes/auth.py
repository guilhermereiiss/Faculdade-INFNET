from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

import database.db as db
from models.usuario import UsuarioCreate, UsuarioDB, TokenResponse, TokenMFAResponse
from auth.security import (
    hash_password, verify_password, criar_token,
    SCOPES_POR_PAPEL, decodificar_token
)

router = APIRouter(prefix="/auth", tags=["auth"])


# ── Registro de usuário ───────────────────────────────────────────────────────
@router.post("/registrar", status_code=201, response_model=dict)
def registrar(dados: UsuarioCreate):
    if db.obter_usuario(dados.username):
        raise HTTPException(status_code=400, detail="Username já existe")
    usuario = UsuarioDB(
        username=dados.username,
        hashed_password=hash_password(dados.password),
        papel=dados.papel,
        mfa_habilitado=(dados.papel == "admin"),
    )
    db.criar_usuario(usuario)
    return {"mensagem": f"Usuário '{dados.username}' criado com papel '{dados.papel}'"}


# ── Login (OAuth2PasswordBearer) ──────────────────────────────────────────────
@router.post("/login", response_model=TokenMFAResponse)
def login(form: OAuth2PasswordRequestForm = Depends()):
    usuario = db.obter_usuario(form.username)
    if not usuario or not verify_password(form.password, usuario.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    escopos = SCOPES_POR_PAPEL.get(usuario.papel, [])

    # Admin com MFA: emite token com flag mfa_pendente=True e escopo limitado
    if usuario.papel == "admin" and usuario.mfa_habilitado:
        token = criar_token(
            sub=usuario.username,
            papel=usuario.papel,
            escopos=["eventos:read"],  # escopo reduzido até MFA ser verificado
            extra_claims={"mfa_pendente": True},
        )
        return TokenMFAResponse(access_token=token, mfa_pendente=True)

    token = criar_token(sub=usuario.username, papel=usuario.papel, escopos=escopos)
    return TokenMFAResponse(access_token=token, mfa_pendente=False)


# ── Verificação MFA (simulado) ────────────────────────────────────────────────
class MFAVerify(BaseModel):
    token_parcial: str   # token recebido no login
    codigo_mfa: str      # código TOTP simulado (aceita "123456" para demo)


@router.post("/mfa/verificar", response_model=TokenResponse)
def verificar_mfa(dados: MFAVerify):
    """
    Exercício 7 — fluxo MFA simulado para administradores.
    Em produção, o código seria validado contra um TOTP real (ex: pyotp).
    Para demonstração, o código aceito é '123456'.
    """
    try:
        payload = decodificar_token(dados.token_parcial)
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido")

    if not payload.get("mfa_pendente"):
        raise HTTPException(status_code=400, detail="MFA não está pendente para este token")

    if dados.codigo_mfa != "123456":  # simulação — em prod: pyotp.TOTP(secret).verify()
        raise HTTPException(status_code=401, detail="Código MFA inválido")

    username = payload["sub"]
    usuario = db.obter_usuario(username)
    escopos = SCOPES_POR_PAPEL.get(usuario.papel, [])

    # Emite token completo sem flag mfa_pendente
    token = criar_token(
        sub=username,
        papel=usuario.papel,
        escopos=escopos,
        extra_claims={"mfa_verificado": True},
    )
    return TokenResponse(access_token=token)


# ── Token M2M (Client Credentials — Exercício 8) ─────────────────────────────
class M2MCredentials(BaseModel):
    client_id: str
    client_secret: str
    scope: str = "m2m:read"


@router.post("/m2m/token", response_model=TokenResponse)
def token_m2m(creds: M2MCredentials):
    """
    Exercício 8 — OAuth 2.0 Client Credentials Flow para integração M2M.
    Parceiros externos se autenticam com client_id + client_secret, sem usuário humano.
    """
    # Credenciais do parceiro (em prod: banco de clients OAuth registrados)
    PARCEIROS = {
        "parceiro-externo": "secret-parceiro-xpto-2025",
    }

    if PARCEIROS.get(creds.client_id) != creds.client_secret:
        raise HTTPException(status_code=401, detail="Credenciais M2M inválidas")

    # Escopos permitidos para M2M — nunca admin:all
    escopos_permitidos = {"m2m:read", "m2m:write"}
    escopos_solicitados = set(creds.scope.split())
    escopos_concedidos = list(escopos_solicitados & escopos_permitidos)

    if not escopos_concedidos:
        raise HTTPException(status_code=400, detail="Escopo não permitido para M2M")

    token = criar_token(
        sub=creds.client_id,
        papel="m2m_parceiro",
        escopos=escopos_concedidos,
        expire_minutes=60,
        extra_claims={
            "client_id": creds.client_id,
            "grant_type": "client_credentials",
        },
    )
    return TokenResponse(access_token=token)
