from typing import List, Dict, Any
from fastapi import APIRouter, Depends, Security
from pydantic import BaseModel, ConfigDict, Field
from auth.dependencies import verificar_m2m_laboratorio

router = APIRouter(prefix="/laboratorio", tags=["Integração M2M — Laboratório Parceiro"])


class AgendamentoExameM2M(BaseModel):
    model_config = ConfigDict(extra="forbid")

    codigo_pedido_laboratorio: str = Field(..., min_length=5, max_length=50)
    data_hora_coleta: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$")
    tipo_exame: str = Field(..., min_length=3, max_length=100)


@router.get(
    "/horarios-disponiveis",
    response_model=List[Dict[str, Any]],
    summary="Consulta M2M de horários vagos para coletas laboratoriais",
)
def consultar_horarios_disponiveis(
    payload_m2m: dict = Security(
        verificar_m2m_laboratorio,
        scopes=["laboratorio:disponibilidade"],
    ),
) -> List[Dict[str, Any]]:
    """
    Exercício 7 — Integração Máquina-a-Máquina (M2M):
    Permite que o laboratório parceiro consulte horários vagos para alinhar coletas de exames.
    O endpoint não expõe nenhum dado pessoal ou prontuário de pacientes da clínica.
    """
    # Retorna slots de disponibilidade parametrizados da clínica
    return [
        {
            "slot_id": 101,
            "data_hora": "2026-09-21T08:00:00",
            "especialidade": "Coleta de Sangue / Bioquímica",
            "unidade": "Unidade Central",
            "disponivel": True,
        },
        {
            "slot_id": 102,
            "data_hora": "2026-09-21T09:30:00",
            "especialidade": "Exames de Imagem / Ultrassonografia",
            "unidade": "Unidade Central",
            "disponivel": True,
        },
        {
            "slot_id": 103,
            "data_hora": "2026-09-21T14:00:00",
            "especialidade": "Eletrocardiograma (ECG)",
            "unidade": "Anexo Cardio",
            "disponivel": True,
        },
    ]


@router.post(
    "/confirmar-coleta",
    status_code=201,
    summary="Confirmação M2M de agendamento de exame laboratorial",
)
def confirmar_coleta_exame(
    dados: AgendamentoExameM2M,
    payload_m2m: dict = Security(
        verificar_m2m_laboratorio,
        scopes=["laboratorio:exames"],
    ),
) -> Dict[str, Any]:
    """
    Exercício 7 — Registro de coleta externa pelo laboratório parceiro.
    Exige escopo OAuth específico 'laboratorio:exames'.
    """
    return {
        "status": "confirmado",
        "codigo_protocolo": f"LAB-CONF-{dados.codigo_pedido_laboratorio}",
        "data_hora_confirmada": dados.data_hora_coleta,
        "mensagem": "Coleta laboratorial agendada com sucesso no sistema da clínica.",
    }
