from fastapi.testclient import TestClient


def test_bola_medico_bloqueado_ao_acessar_consulta_de_outro_medico(
    client: TestClient,
    headers_medico1: dict,
    headers_medico2: dict,
    headers_admin: dict,
):
    """
    Exercício 8, 9 & 12 — Mitigação de BOLA (Broken Object Level Authorization - OWASP API1:2023):
    - Consulta 1 pertence ao Dr. Carlos (medico 1).
    - Consulta 2 pertence à Dra. Ana (medico 2).
    - Dra. Ana tenta acessar a Consulta 1 trocando apenas o ID na URL -> HTTP 403 FORBIDDEN.
    - Dr. Carlos acessa a Consulta 1 -> HTTP 200 OK.
    - Administrador acessa a Consulta 1 -> HTTP 200 OK.
    """
    # 1. Médico 1 acessa sua própria consulta (sucesso)
    resp_propria = client.get("/consultas/1", headers=headers_medico1)
    assert resp_propria.status_code == 200
    assert resp_propria.json()["id"] == 1

    # 2. Médico 2 tenta acessar a consulta do Médico 1 (tentativa de BOLA)
    resp_bola = client.get("/consultas/1", headers=headers_medico2)
    assert resp_bola.status_code == 403
    assert "Acesso negado" in resp_bola.json()["detail"]

    # 3. Administrador tem visão autorizada
    resp_admin = client.get("/consultas/1", headers=headers_admin)
    assert resp_admin.status_code == 200


def test_mass_assignment_rejeitado_via_extra_forbid(
    client: TestClient,
    headers_medico1: dict,
):
    """
    Exercício 9 & 12 — Prevenção de Mass Assignment (OWASP API3:2023):
    O envio de campos não declarados ou internos de auditoria (ex.: auditoria_modificado_por,
    auditoria_versao_registro) deve ser sumariamente REJEITADO com HTTP 422 Unprocessable Entity
    graças à configuração model_config = ConfigDict(extra='forbid').
    """
    payload_malicioso = {
        "paciente_id": 1,
        "profissional_id": 1,
        "data_hora": "2026-09-25T14:30:00",
        "motivo": "Consulta padrão",
        # Campos maliciosos injetados:
        "auditoria_criado_por": "hacker_injetado",
        "auditoria_modificado_por": "admin_forjado",
        "auditoria_versao_registro": 999,
        "campo_inexistente": "exploit",
    }
    response = client.post("/consultas", json=payload_malicioso, headers=headers_medico1)
    assert response.status_code == 422
    erros = response.json()["detail"]
    # Verifica que o erro reporta campos extras proibidos
    campos_extras = [e["loc"][-1] for e in erros if e["type"] == "extra_forbidden"]
    assert len(campos_extras) > 0


def test_validacao_whitelist_e_regex_cpf_invalido(
    client: TestClient,
    headers_recepcao: dict,
):
    """
    Exercício 9 — Validação rigorosa com Whitelist e Regex:
    CPFs com caracteres inválidos, formatação errada ou tamanho diferente de 11 dígitos
    são rejeitados com HTTP 422.
    """
    payload_cpf_invalido = {
        "nome": "Paciente Teste Invalido",
        "cpf": "111.222.333-XX",  # Inválido: contém letras e pontuação
        "data_nascimento": "1990-01-01",
        "telefone": "11988887777",
        "email": "paciente@teste.com",
    }
    response = client.post("/pacientes", json=payload_cpf_invalido, headers=headers_recepcao)
    assert response.status_code == 422


def test_validacao_whitelist_e_regex_crm_invalido(
    client: TestClient,
    headers_admin: dict,
):
    """
    Exercício 9 — CRM com formato inválido é rejeitado.
    """
    payload_crm_invalido = {
        "nome": "Dr. CRM Invalido",
        "crm": "CRM-9999",  # Formato exigido é '123456-UF'
        "especialidade": "Clínico",
        "username": "dr_crm_inv",
        "email": "crm@clinica.com",
    }
    response = client.post("/profissionais", json=payload_crm_invalido, headers=headers_admin)
    assert response.status_code == 422


def test_prevencao_sql_injection_em_consultas(
    client: TestClient,
    headers_medico1: dict,
):
    """
    Exercício 11 — Queries 100% parametrizadas via SQLModel:
    Tentativa de SQL Injection no motivo ou nas buscas é tratada com segurança
    e persistida apenas como texto literal, sem corrupção do banco relacional.
    """
    payload_sqli = {
        "paciente_id": 1,
        "profissional_id": 1,
        "data_hora": "2026-09-28T16:00:00",
        "motivo": "'; DROP TABLE consulta; --",
        "observacoes": "' OR '1'='1",
    }
    response = client.post("/consultas", json=payload_sqli, headers=headers_medico1)
    assert response.status_code == 201
    consulta_criada = response.json()
    assert consulta_criada["motivo"] == "'; DROP TABLE consulta; --"

    # Confirma que a tabela e outras consultas continuam intactas
    resp_lista = client.get("/consultas", headers=headers_medico1)
    assert resp_lista.status_code == 200
    assert len(resp_lista.json()) >= 1


def test_hardening_headers_seguranca(client: TestClient):
    """
    Exercício 10 — Hardening de Rede:
    Verifica a presença obrigatória dos cabeçalhos defensivos HTTP:
    HSTS, X-Frame-Options, X-Content-Type-Options e CSP.
    """
    response = client.get("/")
    assert response.status_code == 200
    headers = response.headers

    assert "Strict-Transport-Security" in headers
    assert "max-age=31536000" in headers["Strict-Transport-Security"]
    assert headers.get("X-Frame-Options") == "DENY"
    assert headers.get("X-Content-Type-Options") == "nosniff"
    assert "Content-Security-Policy" in headers
    assert "frame-ancestors 'none'" in headers["Content-Security-Policy"]


def test_hardening_cors_sem_wildcard(client: TestClient):
    """
    Exercício 10 — CORS com Allowlist Explícita:
    Verifica que origens maliciosas não autorizadas NÃO recebem cabeçalho
    Access-Control-Allow-Origin liberado.
    """
    headers_maliciosos = {
        "Origin": "https://site-invasor-malicioso.com",
    }
    response = client.get("/", headers=headers_maliciosos)
    assert response.status_code == 200
    # A resposta não deve refletir a origem maliciosa
    assert response.headers.get("access-control-allow-origin") != "https://site-invasor-malicioso.com"
    assert response.headers.get("access-control-allow-origin") != "*"
