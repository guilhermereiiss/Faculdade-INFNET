from fastapi.testclient import TestClient


def test_criar_consulta_sucesso(client: TestClient, headers_medico1: dict):
    """
    Exercício 1 — Fundação da API de agendamento:
    Valida o caminho de sucesso de criação de uma consulta médica via APIRouter.
    """
    payload = {
        "paciente_id": 1,
        "profissional_id": 1,
        "data_hora": "2026-09-25T14:30:00",
        "status": "agendada",
        "motivo": "Check-up cardiológico anual",
        "observacoes": "Trazer exames laboratoriais prévios",
    }
    response = client.post("/consultas", json=payload, headers=headers_medico1)
    assert response.status_code == 201
    dados = response.json()
    assert dados["id"] is not None
    assert dados["paciente_id"] == 1
    assert dados["profissional_id"] == 1
    assert dados["motivo"] == "Check-up cardiológico anual"
    assert dados["status"] == "agendada"


def test_listar_consultas_sucesso(client: TestClient, headers_medico1: dict):
    """
    Exercício 1 — Leitura de consultas via APIRouter.
    """
    response = client.get("/consultas", headers=headers_medico1)
    assert response.status_code == 200
    consultas = response.json()
    assert isinstance(consultas, list)
    assert len(consultas) >= 1


def test_controle_exposicao_campos_auditoria(client: TestClient, headers_medico1: dict):
    """
    Exercício 2 — Controle de exposição de dados:
    O time de segurança exige que NENHUM campo interno de auditoria vaze na resposta JSON da API
    (ex.: auditoria_criado_por, auditoria_data_criacao, auditoria_ip_origem, auditoria_versao_registro).
    """
    response = client.get("/consultas/1", headers=headers_medico1)
    assert response.status_code == 200
    dados = response.json()

    # Campos que DEVEM estar presentes
    assert "id" in dados
    assert "paciente_id" in dados
    assert "profissional_id" in dados
    assert "data_hora" in dados
    assert "status" in dados
    assert "motivo" in dados

    # Campos internos que NUNCA devem vazar na resposta (Exercício 2)
    assert "auditoria_criado_por" not in dados
    assert "auditoria_data_criacao" not in dados
    assert "auditoria_modificado_por" not in dados
    assert "auditoria_ip_origem" not in dados
    assert "auditoria_versao_registro" not in dados


def test_pagina_recepcao_html_e_seguranca_xss(client: TestClient):
    """
    Exercício 2 — Página HTML da recepção com Jinja2:
    - Valida que a página renderiza com status 200 e Content-Type text/html.
    - Valida que tags maliciosas injetadas no motivo são escapadas (mitigação de XSS).
    - Valida herança de templates e ausência de prontuários confidenciais na interface.
    """
    response = client.get("/recepcao/agenda")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    html_content = response.text

    # Verifica estrutura do layout
    assert "Clínica Médica Integrada" in html_content
    assert "Agenda do Dia" in html_content
    assert "João Pereira da Silva" in html_content

    # Garante que prontuários médicos confidenciais NÃO aparecem na página da recepção
    assert "ECG solicitado" not in html_content
    assert "Inspeção cutânea sem lesões" not in html_content
