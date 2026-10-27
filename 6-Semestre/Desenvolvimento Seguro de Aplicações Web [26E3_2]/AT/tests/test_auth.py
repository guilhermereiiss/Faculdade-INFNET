from fastapi.testclient import TestClient


def test_login_sucesso_profissional_saude(client: TestClient):
    """
    Exercício 6 — Autenticação de profissional de saúde com credenciais válidas.
    """
    payload = {
        "username": "dr_carlos",
        "password": "Medico@123456",
    }
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 200
    dados = response.json()
    assert "access_token" in dados
    assert dados["token_type"] == "bearer"
    assert dados["papel"] == "profissional_saude"
    assert "consultas:read" in dados["scope"]


def test_login_admin_exige_mfa(client: TestClient):
    """
    Exercício 6 — Contas administrativas exigem MFA obrigatório.
    Sem informar o código MFA, o login deve ser recusado com 403 Forbidden.
    """
    payload_sem_mfa = {
        "username": "admin",
        "password": "Admin@123456",
    }
    response = client.post("/auth/login", json=payload_sem_mfa)
    assert response.status_code == 403
    assert "MFA obrigatório" in response.json()["detail"]


def test_login_admin_sucesso_com_mfa(client: TestClient):
    """
    Exercício 6 — Login de administrador bem-sucedido com código MFA válido.
    """
    payload_com_mfa = {
        "username": "admin",
        "password": "Admin@123456",
        "mfa_code": "123456",
    }
    response = client.post("/auth/login", json=payload_com_mfa)
    assert response.status_code == 200
    dados = response.json()
    assert dados["mfa_verified"] is True
    assert "admin:all" in dados["scope"]


def test_bloqueio_usuario_nao_admin_em_rota_restrita(
    client: TestClient,
    headers_medico1: dict,
    headers_recepcao: dict,
    headers_admin: dict,
):
    """
    Exercício 6 — Teste obrigatório do enunciado:
    Valida que um usuário sem papel de administrador é IMPEDIDO de acessar uma rota restrita
    a administradores (exclusão de paciente ou consultas), retornando HTTP 403 Forbidden.
    """
    # 1. Médico tenta excluir paciente (rota restrita ao admin com escopo 'pacientes:delete')
    response_medico = client.delete("/pacientes/1", headers=headers_medico1)
    assert response_medico.status_code == 403
    assert "Escopo insuficiente" in response_medico.json()["detail"] or "Acesso negado" in response_medico.json()["detail"]

    # 2. Recepcionista tenta excluir paciente
    response_recepcao = client.delete("/pacientes/1", headers=headers_recepcao)
    assert response_recepcao.status_code == 403

    # 3. Administrador autenticado com MFA consegue executar a operação
    response_admin = client.delete("/pacientes/1", headers=headers_admin)
    assert response_admin.status_code == 204


def test_admin_sem_mfa_bloqueado(client: TestClient, headers_admin_sem_mfa: dict):
    """
    Exercício 6 — Valida que se um token de admin não tiver a flag de MFA verificado,
    ele é rejeitado com 403 Forbidden ao acessar rotas protegidas.
    """
    response = client.get("/consultas", headers=headers_admin_sem_mfa)
    assert response.status_code == 403
    assert "MFA" in response.json()["detail"]
