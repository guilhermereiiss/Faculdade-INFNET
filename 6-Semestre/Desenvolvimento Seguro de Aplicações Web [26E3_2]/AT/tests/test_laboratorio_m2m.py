from fastapi.testclient import TestClient


def test_obter_token_m2m_sucesso(client: TestClient):
    """
    Exercício 7 — Emissão de token M2M via Client Credentials.
    """
    payload = {
        "client_id": "laboratorio-parceiro-01",
        "client_secret": "segredo-forte-m2m-lab-2026",
    }
    response = client.post("/auth/m2m/token", json=payload)
    assert response.status_code == 200
    dados = response.json()
    assert "access_token" in dados
    assert dados["papel"] == "m2m_laboratorio"
    assert "laboratorio:disponibilidade" in dados["scope"]


def test_laboratorio_consulta_horarios_disponiveis(
    client: TestClient,
    headers_m2m_laboratorio: dict,
):
    """
    Exercício 7 — Laboratório acessa endpoint M2M autorizado.
    """
    response = client.get(
        "/laboratorio/horarios-disponiveis",
        headers=headers_m2m_laboratorio,
    )
    assert response.status_code == 200
    slots = response.json()
    assert len(slots) > 0
    assert "data_hora" in slots[0]
    assert "especialidade" in slots[0]


def test_laboratorio_bloqueado_de_acessar_prontuarios_e_pacientes(
    client: TestClient,
    headers_m2m_laboratorio: dict,
):
    """
    Exercício 7 — Garantia técnica de escopos:
    O laboratório parceiro NÃO possui os escopos de usuário ('pacientes:read', 'consultas:read').
    Mesmo com token M2M válido, o acesso a rotas confidenciais de pacientes deve ser bloqueado com 403.
    """
    # 1. Tentativa de listar pacientes
    response_pacientes = client.get("/pacientes", headers=headers_m2m_laboratorio)
    assert response_pacientes.status_code in [401, 403]

    # 2. Tentativa de acessar consultas médicas
    response_consultas = client.get("/consultas/1", headers=headers_m2m_laboratorio)
    assert response_consultas.status_code in [401, 403]


def test_profissional_bloqueado_de_acessar_endpoint_m2m(
    client: TestClient,
    headers_medico1: dict,
):
    """
    Exercício 7 — Profissional de saúde humano não possui escopos M2M,
    sendo impedido de operar a interface de máquina do laboratório.
    """
    response = client.get(
        "/laboratorio/horarios-disponiveis",
        headers=headers_medico1,
    )
    assert response.status_code in [401, 403]
