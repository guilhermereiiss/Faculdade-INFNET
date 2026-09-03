from pydantic import BaseModel
from datetime import date
from typing import Optional


class EventoCreate(BaseModel):
    nome: str
    data: date
    organizador: str
    local: str
    descricao: Optional[str] = None


class EventoInterno(EventoCreate):
    id: int
    organizador_id: str
    token_auditoria: str
    owner_username: str  


class EventoResponse(BaseModel):
    id: int
    nome: str
    data: date
    organizador: str
    local: str
    descricao: Optional[str] = None
