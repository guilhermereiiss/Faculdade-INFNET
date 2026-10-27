from typing import Optional
from datetime import datetime, timezone
from pydantic import BaseModel, EmailStr, ConfigDict, Field as PydanticField
from sqlmodel import SQLModel, Field


class Paciente(SQLModel, table=True):
    """
    Entidade de persistência do Paciente.
    Armazena dados pessoais e clínicos sob a égide da LGPD (Art. 5º, II - dados sensíveis).
    Inclui campos internos de auditoria que NÃO devem ser expostos em respostas de API.
    """
    __tablename__ = "paciente"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False)
    cpf: str = Field(index=True, unique=True, nullable=False)
    data_nascimento: str = Field(nullable=False)  # Formato YYYY-MM-DD
    telefone: str = Field(nullable=False)
    email: str = Field(nullable=False)
    endereco: Optional[str] = Field(default=None)
    historico_alergias: Optional[str] = Field(default=None)

    # Campos internos de auditoria e segurança da clínica (Exercício 2 e 9)
    # NUNCA devem ser expostos na resposta JSON nem manipulados via Mass Assignment
    auditoria_criado_por: str = Field(default="sistema")
    auditoria_data_criacao: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    auditoria_ip_origem: Optional[str] = Field(default="127.0.0.1")


class PacienteCreate(BaseModel):
    """
    Schema de validação estrita com extra='forbid' e regex defensivos (Exercício 9).
    """
    model_config = ConfigDict(extra="forbid")

    nome: str = PydanticField(..., min_length=3, max_length=100, pattern=r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$")
    cpf: str = PydanticField(..., pattern=r"^\d{11}$", description="11 dígitos numéricos sem pontuação")
    data_nascimento: str = PydanticField(..., pattern=r"^\d{4}-\d{2}-\d{2}$")
    telefone: str = PydanticField(..., pattern=r"^\+?[0-9]{10,15}$")
    email: EmailStr
    endereco: Optional[str] = PydanticField(default=None, max_length=200)
    historico_alergias: Optional[str] = PydanticField(default=None, max_length=500)


class PacienteUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nome: Optional[str] = PydanticField(default=None, min_length=3, max_length=100, pattern=r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$")
    telefone: Optional[str] = PydanticField(default=None, pattern=r"^\+?[0-9]{10,15}$")
    email: Optional[EmailStr] = None
    endereco: Optional[str] = PydanticField(default=None, max_length=200)
    historico_alergias: Optional[str] = PydanticField(default=None, max_length=500)


class PacienteResponse(BaseModel):
    """
    Response model do Exercício 2 — filtra terminantemente campos de auditoria interna.
    """
    id: int
    nome: str
    cpf: str
    data_nascimento: str
    telefone: str
    email: EmailStr
    endereco: Optional[str] = None
    historico_alergias: Optional[str] = None


class PacientePublico(BaseModel):
    """
    Visualização restrita para a recepção ou parceiros externos.
    """
    id: int
    nome: str
    telefone: str
