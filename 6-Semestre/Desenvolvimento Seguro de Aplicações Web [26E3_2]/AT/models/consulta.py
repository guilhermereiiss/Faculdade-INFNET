from typing import Optional
from datetime import datetime, timezone
from pydantic import BaseModel, ConfigDict, Field as PydanticField
from sqlmodel import SQLModel, Field


class Consulta(SQLModel, table=True):
    """
    Entidade central de agendamento de consultas médicas.
    Contém dados de saúde de pacientes (LGPD) e prontuários diagnósticos.
    Inclui trilha de auditoria interna que NUNCA deve vazar na API pública.
    """
    __tablename__ = "consulta"

    id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: int = Field(foreign_key="paciente.id", nullable=False, index=True)
    profissional_id: int = Field(foreign_key="profissional.id", nullable=False, index=True)
    data_hora: str = Field(nullable=False, index=True)  # ISO 8601: YYYY-MM-DDTHH:MM:SS
    status: str = Field(default="agendada", nullable=False)  # agendada, confirmada, realizada, cancelada
    motivo: str = Field(nullable=False)
    prontuario_diagnostico: Optional[str] = Field(default=None)  # Dado sensível de saúde (LGPD)
    observacoes: Optional[str] = Field(default=None)

    # ── Campos internos de auditoria e controle de integridade (Exercício 2 & 9) ──
    # O time de segurança exige que nenhum desses campos vaze na resposta JSON da API.
    auditoria_criado_por: str = Field(default="sistema")
    auditoria_data_criacao: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    auditoria_modificado_por: Optional[str] = Field(default=None)
    auditoria_ip_origem: Optional[str] = Field(default="127.0.0.1")
    auditoria_versao_registro: int = Field(default=1)


class ConsultaCreate(BaseModel):
    """
    Schema estrito para criação de consultas (Exercício 9).
    extra='forbid' impede Mass Assignment de campos de auditoria ou prontuário indevido.
    """
    model_config = ConfigDict(extra="forbid")

    paciente_id: int = PydanticField(..., gt=0)
    profissional_id: int = PydanticField(..., gt=0)
    data_hora: str = PydanticField(
        ...,
        pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$",
        description="Data e hora no formato ISO 8601 (YYYY-MM-DDTHH:MM:SS)"
    )
    status: Optional[str] = PydanticField(
        default="agendada",
        pattern=r"^(agendada|confirmada|realizada|cancelada)$"
    )
    motivo: str = PydanticField(..., min_length=3, max_length=255)
    observacoes: Optional[str] = PydanticField(default=None, max_length=500)


class ConsultaUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    data_hora: Optional[str] = PydanticField(
        default=None,
        pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$"
    )
    status: Optional[str] = PydanticField(
        default=None,
        pattern=r"^(agendada|confirmada|realizada|cancelada)$"
    )
    motivo: Optional[str] = PydanticField(default=None, min_length=3, max_length=255)
    prontuario_diagnostico: Optional[str] = PydanticField(default=None, max_length=2000)
    observacoes: Optional[str] = PydanticField(default=None, max_length=500)


class ConsultaResponse(BaseModel):
    """
    Response model (Exercício 2):
    Controla exatamente os campos expostos ao consumidor da API.
    OMITE expressamente: auditoria_criado_por, auditoria_data_criacao,
    auditoria_modificado_por, auditoria_ip_origem e auditoria_versao_registro.
    """
    id: int
    paciente_id: int
    profissional_id: int
    data_hora: str
    status: str
    motivo: str
    prontuario_diagnostico: Optional[str] = None
    observacoes: Optional[str] = None


class ConsultaPublicaAgenda(BaseModel):
    """
    Schema minimalista para a recepção ou integração com parceiros (M2M).
    Não expõe dados de prontuário, diagnóstico ou campos internos.
    """
    id: int
    data_hora: str
    status: str
    paciente_nome: str
    profissional_nome: str
    especialidade: str
    motivo: str
