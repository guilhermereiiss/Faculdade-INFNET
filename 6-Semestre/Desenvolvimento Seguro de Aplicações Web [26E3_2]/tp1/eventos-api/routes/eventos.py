from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.evento import EventoCreate, EventoInterno, EventoResponse
import database.db as db

router = APIRouter(prefix="/eventos", tags=["eventos"])

templates = Jinja2Templates(directory="templates")


# ── Rotas JSON ──────────────────────────────────────────────────────────────

@router.get("/", response_model=list[EventoResponse])
def listar_eventos():
    """Lista todos os eventos (resposta filtrada pelo response_model)."""
    return db.listar_eventos()


@router.get("/{evento_id}", response_model=EventoResponse)
def obter_evento(evento_id: int):
    """Retorna um evento pelo ID."""
    evento = db.obter_evento(evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return evento


@router.post("/", response_model=EventoResponse, status_code=201)
def criar_evento(dados: EventoCreate):
    """
    Cria um evento. O response_model garante que campos internos
    (organizador_id, token_auditoria) não sejam expostos na resposta.
    """
    return db.criar_evento(dados)


@router.delete("/{evento_id}", status_code=204)
def deletar_evento(evento_id: int):
    """Remove um evento pelo ID."""
    if not db.deletar_evento(evento_id):
        raise HTTPException(status_code=404, detail="Evento não encontrado")


# ── Rota sem response_model (demonstração do risco — Exercício 3) ─────────

@router.post("/inseguro/criar")
def criar_evento_sem_response_model(dados: EventoCreate):
    """
    ⚠️  APENAS PARA DEMONSTRAÇÃO (Exercício 3).
    Sem response_model: campos internos como token_auditoria e organizador_id
    são retornados diretamente, expondo dados sensíveis ao cliente.
    """
    evento: EventoInterno = db.criar_evento(dados)
    return evento  # retorna o objeto completo — token_auditoria e organizador_id vazam!


# ── Rotas HTML (Exercícios 5 e 6) ───────────────────────────────────────────

@router.get("/html/lista", response_class=HTMLResponse)
def listar_eventos_html(request: Request):
    """Renderiza a lista de eventos como HTML via Jinja2."""
    eventos = db.listar_eventos()
    return templates.TemplateResponse(
        "eventos/lista.html",
        {"request": request, "eventos": eventos},
    )


@router.get("/html/{evento_id}", response_class=HTMLResponse)
def detalhe_evento_html(request: Request, evento_id: int):
    """Renderiza a página de detalhe de um evento."""
    evento = db.obter_evento(evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return templates.TemplateResponse(
        "eventos/detalhe.html",
        {"request": request, "evento": evento},
    )
