import re
from fastapi import APIRouter, HTTPException, Depends, Security, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from models.evento import EventoCreate, EventoResponse, InscricaoCreate, InscricaoResponse
from models.usuario import Usuario
from auth.dependencies import get_usuario_atual, verificar_ownership, verificar_ownership_inscricao
from database.db import (
    get_session, listar_eventos, obter_evento, criar_evento, atualizar_evento,
    deletar_evento, buscar_eventos_por_nome, listar_inscricoes, obter_inscricao,
    criar_inscricao, listar_comentarios, adicionar_comentario,
)

router = APIRouter(prefix="/eventos", tags=["eventos"])
templates = Jinja2Templates(directory="templates")

# Exercício 1 — whitelist de caracteres permitidos no parâmetro de busca
# Permite: letras (incluindo acentuadas), números, espaço, hífen, ponto, vírgula
_BUSCA_PATTERN = re.compile(r"^[a-zA-ZÀ-ÖØ-öø-ÿ0-9 \-.,]{1,100}$")


# ── Rotas JSON ───────────────────────────────────────────────────────────────

@router.get("/", response_model=list[EventoResponse])
def listar(
    _: Usuario = Security(get_usuario_atual, scopes=["eventos:read"]),
    session: Session = Depends(get_session),
):
    return listar_eventos(session)


@router.get("/buscar", response_model=list[EventoResponse])
def buscar(
    nome: str = Query(..., description="Termo de busca (apenas letras, números e espaços)"),
    _: Usuario = Security(get_usuario_atual, scopes=["eventos:read"]),
    session: Session = Depends(get_session),
):
    """
    Exercício 1 — busca de eventos por nome.

    Validação por whitelist + regex ANTES de qualquer processamento:
    - Rejeita caracteres especiais (aspas simples, hífens SQL, parênteses etc.)
    - A query interna usa parâmetros de bind (nunca concatenação de string)
    """
    if not _BUSCA_PATTERN.match(nome):
        raise HTTPException(
            status_code=400,
            detail=(
                "Parâmetro de busca inválido. "
                "Use apenas letras, números, espaço, hífen, ponto ou vírgula."
            ),
        )
    return buscar_eventos_por_nome(session, nome)


@router.get("/{evento_id}", response_model=EventoResponse)
def obter(
    evento_id: int,
    _: Usuario = Security(get_usuario_atual, scopes=["eventos:read"]),
    session: Session = Depends(get_session),
):
    evento = obter_evento(session, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return evento


@router.post("/", response_model=EventoResponse, status_code=201)
def criar(
    dados: EventoCreate,
    usuario: Usuario = Security(get_usuario_atual, scopes=["eventos:write"]),
    session: Session = Depends(get_session),
):
    return criar_evento(session, dados, owner_username=usuario.username)


@router.put("/{evento_id}", response_model=EventoResponse)
def editar(
    evento_id: int,
    dados: EventoCreate,
    usuario: Usuario = Security(get_usuario_atual, scopes=["eventos:write"]),
    session: Session = Depends(get_session),
):
    verificar_ownership(evento_id, usuario, session)
    atualizado = atualizar_evento(session, evento_id, dados)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return atualizado


@router.delete("/{evento_id}", status_code=204)
def deletar(
    evento_id: int,
    usuario: Usuario = Security(get_usuario_atual, scopes=["eventos:delete"]),
    session: Session = Depends(get_session),
):
    verificar_ownership(evento_id, usuario, session)
    if not deletar_evento(session, evento_id):
        raise HTTPException(status_code=404, detail="Evento não encontrado")


# ── Inscrições (BOLA — Ex 3 & 4) ─────────────────────────────────────────────

@router.get("/inscricoes/todas", response_model=list[InscricaoResponse], tags=["inscricoes"])
def listar_todas_inscricoes(
    usuario: Usuario = Security(get_usuario_atual, scopes=["admin:all"]),
    session: Session = Depends(get_session),
):
    """Apenas admins podem listar todas as inscrições."""
    return listar_inscricoes(session)


@router.post("/inscricoes/", response_model=InscricaoResponse, status_code=201, tags=["inscricoes"])
def inscrever(
    dados: InscricaoCreate,
    usuario: Usuario = Security(get_usuario_atual, scopes=["eventos:read"]),
    session: Session = Depends(get_session),
):
    evento = obter_evento(session, dados.evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return criar_inscricao(session, dados.evento_id, owner_username=usuario.username)


@router.get("/inscricoes/{inscricao_id}", response_model=InscricaoResponse, tags=["inscricoes"])
def obter_inscricao_por_id(
    inscricao_id: int,
    usuario: Usuario = Security(get_usuario_atual, scopes=["eventos:read"]),
    session: Session = Depends(get_session),
):
    """
    Exercício 3 — BOLA corrigido.
    Antes: qualquer usuário autenticado acessava GET /inscricoes/{id} de qualquer outro.
    Agora: verificar_ownership_inscricao garante que só o dono (ou admin) acessa.
    """
    inscricao = obter_inscricao(session, inscricao_id)
    if not inscricao:
        raise HTTPException(status_code=404, detail="Inscrição não encontrada")

    # Exercício 3 & 4 — verificação de ownership centralizada
    verificar_ownership_inscricao(inscricao, usuario)
    return inscricao


# ── Rotas HTML com comentários (Ex 5 — XSS stored) ───────────────────────────

@router.get("/html/lista", response_class=HTMLResponse)
def listar_html(
    request: Request,
    _: Usuario = Security(get_usuario_atual, scopes=["eventos:read"]),
    session: Session = Depends(get_session),
):
    eventos = listar_eventos(session)
    return templates.TemplateResponse(
        "eventos/lista.html",
        {"request": request, "eventos": eventos},
    )


@router.get("/html/{evento_id}", response_class=HTMLResponse)
def detalhe_html(
    request: Request,
    evento_id: int,
    _: Usuario = Security(get_usuario_atual, scopes=["eventos:read"]),
    session: Session = Depends(get_session),
):
    evento = obter_evento(session, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    comentarios = listar_comentarios(evento_id)
    return templates.TemplateResponse(
        "eventos/detalhe.html",
        {"request": request, "evento": evento, "comentarios": comentarios},
    )


@router.post("/html/{evento_id}/comentario", response_class=HTMLResponse)
def postar_comentario(
    request: Request,
    evento_id: int,
    _: Usuario = Security(get_usuario_atual, scopes=["eventos:read"]),
    session: Session = Depends(get_session),
):
    """
    Exercício 5 — comentário é armazenado como texto puro.
    O escape XSS acontece no Jinja2 (auto-escape em .html), não aqui.
    """
    import asyncio
    from fastapi import Form

    # Rota de demo — comentário via form param
    raise HTTPException(status_code=405, detail="Use POST JSON abaixo")


@router.post("/html/{evento_id}/comentar", tags=["comentarios"])
def comentar(
    evento_id: int,
    comentario: str,
    _: Usuario = Security(get_usuario_atual, scopes=["eventos:read"]),
    session: Session = Depends(get_session),
):
    """
    Exercício 5 — armazena comentário (pode conter payload XSS para demonstração).
    O output encoding é feito pelo Jinja2 ao renderizar o template HTML.
    """
    evento = obter_evento(session, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    adicionar_comentario(evento_id, comentario)
    return {"mensagem": "Comentário adicionado", "comentario_armazenado": comentario}
