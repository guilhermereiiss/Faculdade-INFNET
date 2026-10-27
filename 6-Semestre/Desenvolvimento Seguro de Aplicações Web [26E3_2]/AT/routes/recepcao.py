from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from database.db import (
    get_session,
    obter_paciente_por_id,
    obter_profissional_por_id,
)
from models.consulta import Consulta

router = APIRouter(prefix="/recepcao", tags=["Interface da Recepção (HTML / Jinja2)"])

# Configuração segura do Jinja2: autoescape ativo por padrão contra ataques de XSS (Exercício 2 & 9)
templates = Jinja2Templates(directory="templates", autoescape=True)


@router.get("/agenda", response_class=HTMLResponse, summary="Página HTML da agenda do dia com herança e proteção XSS")
def exibir_agenda_dia(
    request: Request,
    data: Optional[str] = None,
    session: Session = Depends(get_session),
) -> HTMLResponse:
    """
    Exercício 2 & 9 — Página HTML segura para a recepção:
    - Utiliza herança de templates (base.html -> agenda.html).
    - Exibe dados formatados de consultas do dia de forma estritamente protegida contra XSS (auto-escape nativo do Jinja2).
    - Oculta completamente prontuários médicos, diagnósticos e metadados de auditoria interna.
    """
    statement = select(Consulta)
    consultas = session.exec(statement).all()

    dados_formatados: List[Dict[str, Any]] = []
    for c in consultas:
        paciente = obter_paciente_por_id(session, c.paciente_id)
        profissional = obter_profissional_por_id(session, c.profissional_id)

        dados_formatados.append({
            "id": c.id,
            "data_hora": c.data_hora.replace("T", " às "),
            "status": c.status,
            "motivo": c.motivo,
            "paciente_nome": paciente.nome if paciente else f"Paciente #{c.paciente_id}",
            "paciente_telefone": paciente.telefone if paciente else "N/A",
            "profissional_nome": profissional.nome if profissional else f"Dr(a) #{c.profissional_id}",
            "especialidade": profissional.especialidade if profissional else "Clínica Geral",
        })

    return templates.TemplateResponse(
        request=request,
        name="agenda.html",
        context={
            "consultas": dados_formatados,
            "data_selecionada": data or "Hoje",
        },
    )
