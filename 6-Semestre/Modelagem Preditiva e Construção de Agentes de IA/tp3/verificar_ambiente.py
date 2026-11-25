"""Valida a configuração do ambiente e o carregamento seguro da chave pelo OpenAI Agents SDK."""

import os
import sys

import agents
from agents.models.openai_provider import OpenAIProvider
from dotenv import load_dotenv

PLACEHOLDER_CHAVE = "sk-proj-substitua-pela-sua-chave-aqui"


def verificar_variavel_ambiente() -> bool:
    chave = os.getenv("OPENAI_API_KEY", "").strip()
    if not chave:
        print("[ERRO] Variável OPENAI_API_KEY não encontrada no ambiente nem no arquivo .env.")
        return False
    if chave == PLACEHOLDER_CHAVE:
        print("[ERRO] OPENAI_API_KEY ainda contém o valor de exemplo do .env.example.")
        return False

    print(f"[OK] OPENAI_API_KEY carregada via ambiente/.env (comprimento: {len(chave)} caracteres; valor oculto).")
    return True


def verificar_sdk() -> bool:
    print(f"[OK] OpenAI Agents SDK importado (versão {agents.__version__}).")
    if os.getenv("OPENAI_BASE_URL"):
        agents.set_default_openai_api("chat_completions")
        agents.set_tracing_disabled(True)
    modelo_alvo = os.getenv("OPENAI_DEFAULT_MODEL", "gpt-4o-mini")
    try:
        provedor = OpenAIProvider()
        modelo = provedor.get_model(modelo_alvo)
    except Exception as erro:
        print(f"[ERRO] O SDK não conseguiu inicializar o cliente OpenAI: {erro}")
        return False

    print(f"[OK] OpenAIProvider inicializado e pronto para uso com o modelo '{modelo.model}'.")
    return True


def main() -> int:
    load_dotenv()
    variavel_ok = verificar_variavel_ambiente()
    sdk_ok = verificar_sdk() if variavel_ok else False

    if variavel_ok and sdk_ok:
        print("Ambiente validado com sucesso.")
        return 0

    print("Configure OPENAI_API_KEY no arquivo .env (baseado em .env.example) e tente novamente.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
