from pydantic import BaseModel
from datetime import date
from typing import Optional


# Modelo de entrada (criação)
class EventoCreate(BaseModel):
    nome: str
    data: date
    organizador: str
    local: str
    descricao: Optional[str] = None


# Modelo interno — contém campos que NÃO devem vazar para o cliente
class EventoInterno(EventoCreate):
    id: int
    organizador_id: str       # identificador interno do organizador
    token_auditoria: str      # token interno de rastreamento


# Response model público — apenas o que o cliente pode ver
class EventoResponse(BaseModel):
    id: int
    nome: str
    data: date
    organizador: str
    local: str
    descricao: Optional[str] = None
