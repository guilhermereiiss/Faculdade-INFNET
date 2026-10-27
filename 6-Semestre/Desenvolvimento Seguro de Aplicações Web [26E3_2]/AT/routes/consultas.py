from typing import List
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Security, status
from sqlmodel import Session, select
from database.db import (
    get_session,
    obter_consulta_por_id,
    obter_paciente_por_id,
    obter_profissional_por_id,
    obter_profissional_por_username,
)
from models.consulta import Consulta, ConsultaCreate, ConsultaUpdate, ConsultaResponse
from models.usuario import Usuario
from auth.dependencies import get_usuario_atual, verificar_ownership_consulta

router = APIRouter(prefix="/consultas", tags=["Consultas Médicas"])


@router.post(
    "",
    response_model=ConsultaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criação de agendamento de consulta",
)
def criar_consulta(
    dados: ConsultaCreate,
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["consultas:write"]),
) -> ConsultaResponse:
    """
    Exercício 1 & 9 — Criação segura de consultas:
    - Validação de entrada com extra='forbid' e regex ISO 8601.
    - Verificação de integridade referencial: paciente e profissional devem existir.
    - Prevenção de spoofing de identidade: se for profissional de saúde, só pode criar para seu próprio CRM.
    """
    paciente = obter_paciente_por_id(session, dados.paciente_id)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não encontrado para o ID informado.",
        )

    profissional = obter_profissional_por_id(session, dados.profissional_id)
    if not profissional:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profissional de saúde não encontrado para o ID informado.",
        )

    # Restrição de criação para profissionais de saúde: só podem criar consultas para si mesmos
    if usuario_atual.papel == "profissional_saude":
        prof_logado = obter_profissional_por_username(session, usuario_atual.username)
        if not prof_logado or prof_logado.id != dados.profissional_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Profissionais de saúde só podem agendar consultas vinculadas a si mesmos.",
            )

    nova_consulta = Consulta(
        paciente_id=dados.paciente_id,
        profissional_id=dados.profissional_id,
        data_hora=dados.data_hora,
        status=dados.status or "agendada",
        motivo=dados.motivo,
        observacoes=dados.observacoes,
        auditoria_criado_por=usuario_atual.username,
        auditoria_data_criacao=datetime.now(timezone.utc).isoformat(),
        auditoria_versao_registro=1,
    )

    session.add(nova_consulta)
    session.commit()
    session.refresh(nova_consulta)
    return nova_consulta


@router.get(
    "",
    response_model=List[ConsultaResponse],
    summary="Listagem de consultas filtrada por papel e autorização",
)
def listar_consultas(
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["consultas:read"]),
) -> List[ConsultaResponse]:
    """
    Exercício 1, 2 & 6 — Listagem com controle de acesso:
    - Administradores e recepcionistas visualizam a agenda completa.
    - Profissionais de saúde visualizam APENAS as suas próprias consultas (filtro automático).
    - Response model oculta rigorosamente metadados internos de auditoria.
    """
    if usuario_atual.papel in ["admin", "recepcionista"]:
        consultas = session.exec(select(Consulta)).all()
    else:
        prof_logado = obter_profissional_por_username(session, usuario_atual.username)
        if not prof_logado:
            return []
        statement = select(Consulta).where(Consulta.profissional_id == prof_logado.id)
        consultas = session.exec(statement).all()

    return list(consultas)


@router.get(
    "/{consulta_id}",
    response_model=ConsultaResponse,
    summary="Obter consulta por ID com verificação de ownership (Anti-BOLA)",
)
def obter_consulta(
    consulta_id: int,
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["consultas:read"]),
) -> ConsultaResponse:
    """
    Exercício 6, 8 & 9 — Mitigação de BOLA (OWASP API1:2023):
    Apenas o médico responsável pela consulta ou o administrador podem visualizá-la.
    Tentativas de manipulação de ID por outros profissionais geram 403 Forbidden.
    """
    consulta = verificar_ownership_consulta(consulta_id, usuario_atual, session)
    return consulta


@router.put(
    "/{consulta_id}",
    response_model=ConsultaResponse,
    summary="Atualização de consulta com controle de mutação e ownership",
)
def atualizar_consulta(
    consulta_id: int,
    dados: ConsultaUpdate,
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["consultas:write"]),
) -> ConsultaResponse:
    """
    Exercício 6, 8 & 9 — Atualização segura:
    - Prevenção de Mass Assignment via extra='forbid'.
    - Ownership check: impede edição de consultas de terceiros.
    - Recepcionistas não podem editar campos de prontuário médico.
    """
    consulta = verificar_ownership_consulta(consulta_id, usuario_atual, session)

    if dados.prontuario_diagnostico is not None:
        if usuario_atual.papel not in ["profissional_saude", "admin"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Apenas profissionais de saúde ou administradores podem atualizar prontuários.",
            )
        consulta.prontuario_diagnostico = dados.prontuario_diagnostico

    if dados.data_hora is not None:
        consulta.data_hora = dados.data_hora
    if dados.status is not None:
        consulta.status = dados.status
    if dados.motivo is not None:
        consulta.motivo = dados.motivo
    if dados.observacoes is not None:
        consulta.observacoes = dados.observacoes

    # Atualiza trilha de auditoria interna
    consulta.auditoria_modificado_por = usuario_atual.username
    consulta.auditoria_versao_registro += 1

    session.add(consulta)
    session.commit()
    session.refresh(consulta)
    return consulta


@router.delete(
    "/{consulta_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Cancelamento e exclusão de consulta médica",
)
def deletar_consulta(
    consulta_id: int,
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["consultas:delete"]),
) -> None:
    """
    Exercício 1 & 6 — Cancelamento restrito:
    Exige escopo estrito 'consultas:delete' (restrito a administradores).
    """
    consulta = obter_consulta_por_id(session, consulta_id)
    if not consulta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Consulta médica não encontrada.",
        )

    session.delete(consulta)
    session.commit()
    return None
