from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field as PydanticField
from sqlmodel import SQLModel, Field


class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    papel: str = Field(nullable=False)  # "recepcionista", "profissional_saude", "admin"
    crm: Optional[str] = Field(default=None, index=True)
    is_active: bool = Field(default=True)
    mfa_enabled: bool = Field(default=False)
    mfa_secret: Optional[str] = Field(default=None)


class UsuarioCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    username: str = PydanticField(..., min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_.-]+$")
    email: EmailStr
    password: str = PydanticField(..., min_length=8, max_length=128)
    papel: str = PydanticField(..., pattern=r"^(recepcionista|profissional_saude|admin)$")
    crm: Optional[str] = PydanticField(default=None, pattern=r"^\d{4,6}-[A-Z]{2}$")
    mfa_enabled: Optional[bool] = False


class UsuarioResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    papel: str
    crm: Optional[str] = None
    is_active: bool
    mfa_enabled: bool


class LoginRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    username: str
    password: str
    mfa_code: Optional[str] = None


class M2MTokenRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    client_id: str
    client_secret: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    scope: str
    papel: str
    mfa_verified: bool = False


class TokenData(BaseModel):
    sub: Optional[str] = None
    papel: Optional[str] = None
    scopes: list[str] = []
    crm: Optional[str] = None
    mfa_verified: bool = False
