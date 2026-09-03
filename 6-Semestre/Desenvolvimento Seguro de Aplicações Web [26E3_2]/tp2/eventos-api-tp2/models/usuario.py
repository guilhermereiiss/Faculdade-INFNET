from pydantic import BaseModel
from typing import Literal


class UsuarioCreate(BaseModel):
    username: str
    password: str
    papel: Literal["organizador", "participante", "admin"] = "organizador"


class UsuarioDB(BaseModel):
    username: str
    hashed_password: str
    papel: Literal["organizador", "participante", "admin"]
    mfa_habilitado: bool = False


class UsuarioResponse(BaseModel):
    username: str
    papel: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenMFAResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    mfa_pendente: bool = False
