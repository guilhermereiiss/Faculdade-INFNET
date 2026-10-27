from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any, List
from jose import jwt
from passlib.context import CryptContext
from config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ── Escopos OAuth 2.0 por Papel (Exercício 6 & 7) ────────────────────────────
SCOPES_POR_PAPEL: Dict[str, List[str]] = {
    "recepcionista": [
        "consultas:read",
        "consultas:write",
        "pacientes:read",
        "pacientes:write",
        "recepcao:agenda",
    ],
    "profissional_saude": [
        "consultas:read",
        "consultas:write",
        "pacientes:read",
        "prontuario:read",
        "prontuario:write",
    ],
    "admin": [
        "consultas:read",
        "consultas:write",
        "consultas:delete",
        "pacientes:read",
        "pacientes:write",
        "pacientes:delete",
        "profissionais:read",
        "profissionais:write",
        "admin:all",
    ],
    "m2m_laboratorio": [
        "laboratorio:disponibilidade",
        "laboratorio:exames",
    ],
}


def hash_password(password: str) -> str:
    """Gera hash seguro com bcrypt (salt automático)."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Valida senha em tempo constante contra ataque de temporização."""
    return pwd_context.verify(plain_password, hashed_password)


def criar_token(
    sub: str,
    papel: str,
    escopos: List[str],
    crm: Optional[str] = None,
    mfa_verified: bool = False,
    expire_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES,
    extra_claims: Optional[Dict[str, Any]] = None,
) -> str:
    """
    Cria JWT assinado com claims de segurança e expiração estrita.
    """
    now = datetime.now(timezone.utc)
    payload: Dict[str, Any] = {
        "sub": sub,
        "papel": papel,
        "scope": " ".join(escopos),
        "crm": crm,
        "mfa_verified": mfa_verified,
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=expire_minutes)).timestamp()),
        "iss": "clinica-medica-api",
    }
    if extra_claims:
        payload.update(extra_claims)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decodificar_token(token: str) -> Dict[str, Any]:
    """Decodifica e valida a assinatura e expiração do JWT."""
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], issuer="clinica-medica-api")
