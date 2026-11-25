"""Prova de conceito de um agente simples de política de cancelamento da NeoStream."""

import os

from agents import Agent, Runner, set_default_openai_api, set_tracing_disabled
from dotenv import load_dotenv

INSTRUCOES_POLITICA_CANCELAMENTO = """
Você é o assistente oficial de política de cancelamento da NeoStream, uma plataforma de streaming
por assinatura com os planos Básico, Padrão e Premium.

Regras da política de cancelamento da NeoStream:
1. Sem fidelidade e sem multa: qualquer assinante pode cancelar a qualquer momento sem taxa de rescisão.
2. Acesso após cancelamento: o acesso permanece ativo até o final do ciclo de cobrança já pago;
   não há cobrança no ciclo seguinte.
3. Direito de arrependimento: em até 7 dias corridos após a primeira contratação, o assinante pode
   solicitar cancelamento com reembolso integral, independentemente do método de pagamento
   (cartão de crédito, PIX ou boleto).
4. Pagamentos por boleto ou PIX: o acesso termina ao fim do período quitado, sem renovação automática.
5. Alternativas ao cancelamento: o cliente pode pausar a assinatura por até 30 dias ou fazer downgrade
   de plano (por exemplo, de Premium para Padrão ou Básico) antes da próxima fatura.

Responda em português, de forma clara, objetiva e cordial, baseando-se exclusivamente nessas regras.
""".strip()

PERGUNTAS_EXEMPLO = [
    (
        "Se eu cancelar minha assinatura hoje no meio do mês, perco o acesso imediatamente "
        "ou continuo assistindo até o fim do período já pago? Existe alguma multa de fidelidade?"
    ),
    (
        "Contratei o plano Premium há 4 dias pagando com PIX e decidi não continuar. "
        "Tenho direito a reembolso integral ou existe alguma alternativa como reduzir meu plano?"
    ),
]


def criar_agente_cancelamento() -> Agent:
    modelo = os.getenv("OPENAI_DEFAULT_MODEL")
    return Agent(
        name="AssistentePoliticaCancelamentoNeoStream",
        instructions=INSTRUCOES_POLITICA_CANCELAMENTO,
        model=modelo,
    )


def configurar_provedor() -> None:
    if os.getenv("OPENAI_BASE_URL"):
        set_default_openai_api("chat_completions")
        set_tracing_disabled(True)


def main() -> None:
    load_dotenv()
    configurar_provedor()
    agente = criar_agente_cancelamento()

    for indice, pergunta in enumerate(PERGUNTAS_EXEMPLO, start=1):
        resultado = Runner.run_sync(agente, pergunta)
        print(f"=== Pergunta {indice} ===")
        print(pergunta)
        print("\nResposta do agente:")
        print(resultado.final_output)
        print()


if __name__ == "__main__":
    main()
