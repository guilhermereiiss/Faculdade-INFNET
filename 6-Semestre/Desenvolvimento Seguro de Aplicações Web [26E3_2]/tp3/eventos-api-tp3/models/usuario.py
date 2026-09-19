from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from typing import Literal, Optional


class Usuario(SQLModel, table=True):
    username: str = Field(primary_key=True)
    hashed_password: str
    papel: str = "organizador"
    mfa_habilitado: bool = False


class UsuarioCreate(BaseModel):
    username: str
    password: str
    papel: Literal["organizador", "participante", "admin"] = "organizador"

    class Config:
        extra = "forbid"


class UsuarioResponse(BaseModel):
    username: str
    papel: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenMFAResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    mfa_pendente: bool = False
