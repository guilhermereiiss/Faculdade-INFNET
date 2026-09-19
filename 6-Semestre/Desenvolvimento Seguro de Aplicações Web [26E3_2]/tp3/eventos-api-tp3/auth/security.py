from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from config import settings

# Credenciais lidas do .env — nunca hardcoded
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

SCOPES_POR_PAPEL = {
    "participante": ["eventos:read"],
    "organizador":  ["eventos:read", "eventos:write", "eventos:delete"],
    "admin":        ["eventos:read", "eventos:write", "eventos:delete", "admin:all"],
    "m2m_parceiro": ["m2m:read", "m2m:write"],
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def criar_token(
    sub: str,
    papel: str,
    escopos: list[str],
    expire_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES,
    extra_claims: Optional[dict] = None,
) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": sub,
        "papel": papel,
        "scope": " ".join(escopos),
        "iat": now,
        "exp": now + timedelta(minutes=expire_minutes),
    }
    if extra_claims:
        payload.update(extra_claims)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decodificar_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
