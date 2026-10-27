from typing import List
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Security, status
from sqlmodel import Session, select
from database.db import get_session, obter_paciente_por_id, obter_paciente_por_cpf
from models.paciente import Paciente, PacienteCreate, PacienteUpdate, PacienteResponse
from models.usuario import Usuario
from auth.dependencies import get_usuario_atual

router = APIRouter(prefix="/pacientes", tags=["Pacientes (LGPD Dados Sensíveis)"])


@router.post(
    "",
    response_model=PacienteResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastro seguro de pacientes com validação estrita",
)
def cadastrar_paciente(
    dados: PacienteCreate,
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["pacientes:write"]),
) -> PacienteResponse:
    """
    Exercício 9 — Cadastro seguro de pacientes sob a LGPD:
    - Validação com whitelist e regex (CPF de 11 dígitos, telefone internacional/nacional, formato data).
    - extra='forbid' bloqueia injeção de parâmetros não mapeados (Mass Assignment).
    - Impede duplicidade de CPF.
    - Metadados de auditoria gravados separadamente e ocultados da resposta.
    """
    paciente_existente = obter_paciente_por_cpf(session, dados.cpf)
    if paciente_existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe um paciente cadastrado com este CPF.",
        )

    novo_paciente = Paciente(
        nome=dados.nome,
        cpf=dados.cpf,
        data_nascimento=dados.data_nascimento,
        telefone=dados.telefone,
        email=dados.email,
        endereco=dados.endereco,
        historico_alergias=dados.historico_alergias,
        auditoria_criado_por=usuario_atual.username,
        auditoria_data_criacao=datetime.now(timezone.utc).isoformat(),
        auditoria_ip_origem="127.0.0.1",
    )

    session.add(novo_paciente)
    session.commit()
    session.refresh(novo_paciente)
    return novo_paciente


@router.get(
    "",
    response_model=List[PacienteResponse],
    summary="Listagem de pacientes cadastrados",
)
def listar_pacientes(
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["pacientes:read"]),
) -> List[PacienteResponse]:
    """
    Exercício 2 & 9:
    - Acesso protegido por autenticação e escopo OAuth.
    - Response model remove campos de auditoria interna.
    """
    pacientes = session.exec(select(Paciente)).all()
    return list(pacientes)


@router.get(
    "/{paciente_id}",
    response_model=PacienteResponse,
    summary="Obter dados de paciente por ID",
)
def obter_paciente(
    paciente_id: int,
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["pacientes:read"]),
) -> PacienteResponse:
    """
    Consulta parametrizada por ID.
    """
    paciente = obter_paciente_por_id(session, paciente_id)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não localizado no cadastro da clínica.",
        )
    return paciente


@router.put(
    "/{paciente_id}",
    response_model=PacienteResponse,
    summary="Atualização de dados cadastrais do paciente",
)
def atualizar_paciente(
    paciente_id: int,
    dados: PacienteUpdate,
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["pacientes:write"]),
) -> PacienteResponse:
    """
    Atualização com extra='forbid' prevenindo mutação indevida de CPF ou metadados de auditoria.
    """
    paciente = obter_paciente_por_id(session, paciente_id)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não localizado para atualização.",
        )

    if dados.nome is not None:
        paciente.nome = dados.nome
    if dados.telefone is not None:
        paciente.telefone = dados.telefone
    if dados.email is not None:
        paciente.email = dados.email
    if dados.endereco is not None:
        paciente.endereco = dados.endereco
    if dados.historico_alergias is not None:
        paciente.historico_alergias = dados.historico_alergias

    session.add(paciente)
    session.commit()
    session.refresh(paciente)
    return paciente


@router.delete(
    "/{paciente_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Exclusão de cadastro de paciente (Direito ao esquecimento LGPD / Restrito a Administradores)",
)
def deletar_paciente(
    paciente_id: int,
    session: Session = Depends(get_session),
    usuario_atual: Usuario = Security(get_usuario_atual, scopes=["pacientes:delete"]),
) -> None:
    """
    Exercício 6 & 9 — Exclusão restrita a administradores.
    """
    if usuario_atual.papel != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas administradores podem excluir registros de pacientes.",
        )

    paciente = obter_paciente_por_id(session, paciente_id)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não localizado para exclusão.",
        )

    session.delete(paciente)
    session.commit()
    return None
