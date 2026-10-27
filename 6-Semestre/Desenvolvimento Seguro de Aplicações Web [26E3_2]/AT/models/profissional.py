from typing import Optional
from datetime import datetime, timezone
from pydantic import BaseModel, EmailStr, ConfigDict, Field as PydanticField
from sqlmodel import SQLModel, Field


class Profissional(SQLModel, table=True):
    __tablename__ = "profissional"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False)
    crm: str = Field(index=True, unique=True, nullable=False)  # Ex: "123456-SP"
    especialidade: str = Field(nullable=False)
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(nullable=False)

    # Campos de auditoria interna (Exercício 2)
    auditoria_data_criacao: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    auditoria_ip_origem: Optional[str] = Field(default="127.0.0.1")


class ProfissionalCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nome: str = PydanticField(..., min_length=3, max_length=100, pattern=r"^[A-Za-zÀ-ÖØ-öø-ÿ\s.]+$")
    crm: str = PydanticField(..., pattern=r"^\d{4,6}-[A-Z]{2}$", description="CRM no formato 123456-UF")
    especialidade: str = PydanticField(..., min_length=3, max_length=50)
    username: str = PydanticField(..., min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_.-]+$")
    email: EmailStr


class ProfissionalResponse(BaseModel):
    id: int
    nome: str
    crm: str
    especialidade: str
    username: str
    email: EmailStr
