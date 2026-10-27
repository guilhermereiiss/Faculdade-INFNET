from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from jose import JWTError
import pytest


def test_mocking_token_invalido_ou_adulterado(client: TestClient):
    """
    Exercício 13 — Testes unitários com mocking:
    Mocka a função de decodificação de token para simular um token criptograficamente
    adulterado que dispara JWTError, assegurando que o sistema rejeita com 401 Unauthorized.
    """
    with patch("auth.dependencies.decodificar_token") as mock_decode:
        mock_decode.side_effect = JWTError("Assinatura HMAC corrompida")

        fake_headers = {"Authorization": "Bearer token.com.assinatura.falsa"}
        response = client.get("/consultas", headers=fake_headers)

        assert response.status_code == 401
        assert "Credenciais inválidas" in response.json()["detail"]
        mock_decode.assert_called_once()


def test_mocking_autorizacao_ownership_consulta(client: TestClient, headers_medico1: dict):
    """
    Exercício 13 — Mocking da verificação de ownership:
    Valida a lógica de isolamento sem depender do estado físico do banco de dados.
    """
    with patch("routes.consultas.verificar_ownership_consulta") as mock_ownership:
        mock_consulta = MagicMock()
        mock_consulta.id = 999
        mock_consulta.paciente_id = 1
        mock_consulta.profissional_id = 1
        mock_consulta.data_hora = "2026-09-25T14:00:00"
        mock_consulta.status = "agendada"
        mock_consulta.motivo = "Consulta mockada com sucesso"
        mock_consulta.prontuario_diagnostico = "Prontuario mockado"
        mock_consulta.observacoes = "Observacao"

        mock_ownership.return_value = mock_consulta

        response = client.get("/consultas/999", headers=headers_medico1)
        assert response.status_code == 200
        dados = response.json()
        assert dados["id"] == 999
        assert dados["motivo"] == "Consulta mockada com sucesso"
        mock_ownership.assert_called_once()


def test_mocking_falha_banco_relacional_na_criacao(client: TestClient, headers_medico1: dict):
    """
    Exercício 13 — Mocking de falha de persistência:
    Simula uma exceção no momento do commit da sessão, verificando tratamento defensivo.
    """
    payload = {
        "paciente_id": 1,
        "profissional_id": 1,
        "data_hora": "2026-09-29T10:00:00",
        "motivo": "Consulta com falha simulada",
    }
    with patch("sqlmodel.Session.commit") as mock_commit:
        mock_commit.side_effect = Exception("Falha simulada de I/O no banco")

        with pytest.raises(Exception) as exc_info:
            client.post("/consultas", json=payload, headers=headers_medico1)

        assert "Falha simulada de I/O" in str(exc_info.value)
