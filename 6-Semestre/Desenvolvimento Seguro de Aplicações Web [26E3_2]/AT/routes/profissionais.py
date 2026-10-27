from typing import List
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Security, status
from sqlmodel import Session, select
from database.db import (
    get_session,
    obter_profissional_por_id,
    obter_profissional_por_crm,
    obter_profissional_por_username,
)
from models.profissional import Profissional, ProfissionalCreate, ProfissionalResponse
from models.usuario import Usuario
from auth.dependencies import get_usuario_atual

router = APIRouter(prefix="/profissionais", tags=["Profissionais de Saúde"])


@router.post(
    "",
    response_model=ProfissionalResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastro de profissional de saúde com validação de CRM e extra='forbid'",
)
def cadastrar_profissional(
    dados: ProfissionalCreate,
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["profissionais:write"]),
) -> ProfissionalResponse:
    """
    Exercício 9 — Validação rigorosa de CRM e dados cadastrais.
    """
    if obter_profissional_por_crm(session, dados.crm):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="CRM já cadastrado para outro profissional de saúde.",
        )

    if obter_profissional_por_username(session, dados.username):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Nome de usuário já vinculado a outro profissional.",
        )

    novo_profissional = Profissional(
        nome=dados.nome,
        crm=dados.crm,
        especialidade=dados.especialidade,
        username=dados.username,
        email=dados.email,
        auditoria_data_criacao=datetime.now(timezone.utc).isoformat(),
        auditoria_ip_origem="127.0.0.1",
    )

    session.add(novo_profissional)
    session.commit()
    session.refresh(novo_profissional)
    return novo_profissional


@router.get(
    "",
    response_model=List[ProfissionalResponse],
    summary="Listagem pública dos médicos e profissionais cadastrados",
)
def listar_profissionais(
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["profissionais:read"]),
) -> List[ProfissionalResponse]:
    profissionais = session.exec(select(Profissional)).all()
    return list(profissionais)


@router.get(
    "/{profissional_id}",
    response_model=ProfissionalResponse,
    summary="Obter profissional por ID",
)
def obter_profissional(
    profissional_id: int,
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["profissionais:read"]),
) -> ProfissionalResponse:
    profissional = obter_profissional_por_id(session, profissional_id)
    if not profissional:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profissional de saúde não encontrado.",
        )
    return profissional
