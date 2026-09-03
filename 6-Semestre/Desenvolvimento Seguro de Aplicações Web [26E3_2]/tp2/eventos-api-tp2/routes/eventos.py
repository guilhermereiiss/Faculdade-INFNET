from fastapi import APIRouter, HTTPException, Depends, Security
from models.evento import EventoCreate, EventoResponse
from models.usuario import UsuarioDB
from auth.dependencies import get_usuario_atual, verificar_ownership
import database.db as db

router = APIRouter(prefix="/eventos", tags=["eventos"])


@router.get("/", response_model=list[EventoResponse])
def listar_eventos(
    _: UsuarioDB = Security(get_usuario_atual, scopes=["eventos:read"])
):
    return db.listar_eventos()


@router.get("/{evento_id}", response_model=EventoResponse)
def obter_evento(
    evento_id: int,
    _: UsuarioDB = Security(get_usuario_atual, scopes=["eventos:read"]),
):
    evento = db.obter_evento(evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return evento


@router.post("/", response_model=EventoResponse, status_code=201)
def criar_evento(
    dados: EventoCreate,
    usuario: UsuarioDB = Security(get_usuario_atual, scopes=["eventos:write"]),
):
    return db.criar_evento(dados, owner_username=usuario.username)


@router.put("/{evento_id}", response_model=EventoResponse)
def editar_evento(
    evento_id: int,
    dados: EventoCreate,
    usuario: UsuarioDB = Security(get_usuario_atual, scopes=["eventos:write"]),
):
    verificar_ownership(evento_id, usuario)
    atualizado = db.atualizar_evento(evento_id, dados)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return atualizado

@router.delete("/{evento_id}", status_code=204)
def deletar_evento(
    evento_id: int,
    usuario: UsuarioDB = Security(get_usuario_atual, scopes=["eventos:delete"]),
):
    verificar_ownership(evento_id, usuario)
    db.deletar_evento(evento_id)

@router.post("/inseguro/criar")
def criar_evento_sem_response_model(dados: EventoCreate):
    return db.criar_evento(dados, owner_username="demo")
