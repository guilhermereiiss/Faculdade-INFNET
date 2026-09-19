from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from datetime import date
from typing import Optional


# ── Tabela de eventos ────────────────────────────────────────────────────────

class EventoBase(SQLModel):
    nome: str = Field(min_length=1, max_length=200)
    data: date
    organizador: str = Field(min_length=1, max_length=100)
    local: str = Field(min_length=1, max_length=200)
    descricao: Optional[str] = Field(default=None, max_length=1000)


class Evento(EventoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    organizador_id: str          # identificador interno — não vaza para o cliente
    token_auditoria: str         # token interno — não vaza para o cliente
    owner_username: str          # username do dono do evento


# ── Schemas de entrada e saída ───────────────────────────────────────────────

class EventoCreate(EventoBase):
    """Input de criação — campos que o cliente pode enviar."""

    class Config:
        extra = "forbid"   # Ex 4: rejeita campos não declarados


class EventoResponse(BaseModel):
    """Output público — campos internos NÃO são expostos."""
    id: int
    nome: str
    data: date
    organizador: str
    local: str
    descricao: Optional[str] = None

    class Config:
        from_attributes = True


# ── Tabela de inscrições ─────────────────────────────────────────────────────

class InscricaoBase(SQLModel):
    evento_id: int = Field(foreign_key="evento.id")


class Inscricao(InscricaoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_username: str          # username de quem se inscreveu


class InscricaoCreate(InscricaoBase):
    class Config:
        extra = "forbid"   # Ex 4: rejeita campos não declarados


class InscricaoResponse(BaseModel):
    id: int
    evento_id: int
    owner_username: str

    class Config:
        from_attributes = True
