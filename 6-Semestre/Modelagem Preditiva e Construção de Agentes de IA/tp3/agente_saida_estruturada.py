"""Agente da NeoStream com saída estruturada validada via Pydantic."""

import os

from agents import Agent, Runner, set_default_openai_api, set_tracing_disabled
from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator

INSTRUCOES_ANALISE_CHURN = """
Você é o agente especialista de retenção e política de cancelamento da NeoStream.
Sua tarefa é analisar perguntas do time de retenção sobre assinantes e risco de cancelamento (churn),
retornando sempre uma avaliação estruturada.

Referências do negócio NeoStream (modelos e políticas internas):
- Fatores que aumentam o risco de churn: maior número de reclamações, baixo tempo de assinatura
  e baixo uso médio semanal em horas.
- Fatores que reduzem o risco de churn: longo tempo de assinatura, uso semanal consistente e
  ausência de reclamações recentes.
- Custo assimétrico: perder um cliente em risco (falso negativo) custa mais do que oferecer uma
  ação de retenção proporcional (contato de suporte, pausa temporária, downgrade de plano ou desconto).
- Política de cancelamento: sem fidelidade, acesso garantido até o fim do ciclo pago, reembolso
  em até 7 dias corridos da primeira contratação e opção de pausa de até 30 dias ou downgrade.

Critérios para o preenchimento dos campos de saída:
- categoria_risco: classifique estritamente como "baixo", "medio" ou "alto".
- recomendacao: indique uma ação objetiva e prática para o time de retenção.
- confianca: número decimal entre 0.0 e 1.0 refletindo o grau de confiança conforme a completude
  dos sinais informados na pergunta.
""".strip()

PERGUNTA_EXEMPLO = (
    "Assinante do plano Básico há 3 meses, uso médio de 2,5 horas por semana e 3 reclamações "
    "registradas no suporte sobre cobrança via boleto. Qual é o risco de cancelamento e que ação "
    "de retenção devemos aplicar?"
)


class RespostaAgente(BaseModel):
    categoria_risco: str = Field(
        description="Categoria de risco de churn do assinante: baixo, medio ou alto."
    )
    recomendacao: str = Field(
        description="Recomendação objetiva de ação para o time de retenção da NeoStream."
    )
    confianca: float = Field(
        description="Nível de confiança da análise em escala decimal entre 0.0 e 1.0."
    )

    @field_validator("confianca")
    @classmethod
    def validar_intervalo_confianca(cls, valor: float) -> float:
        if not 0.0 <= valor <= 1.0:
            raise ValueError("confianca deve estar entre 0.0 e 1.0")
        return valor


def criar_agente_estruturado() -> Agent:
    modelo = os.getenv("OPENAI_DEFAULT_MODEL")
    return Agent(
        name="AgenteRetencaoEstruturadoNeoStream",
        instructions=INSTRUCOES_ANALISE_CHURN,
        output_type=RespostaAgente,
        model=modelo,
    )


def configurar_provedor() -> None:
    if os.getenv("OPENAI_BASE_URL"):
        set_default_openai_api("chat_completions")
        set_tracing_disabled(True)


def main() -> None:
    load_dotenv()
    configurar_provedor()
    agente = criar_agente_estruturado()
    resultado = Runner.run_sync(agente, PERGUNTA_EXEMPLO)
    resposta: RespostaAgente = resultado.final_output

    print("Pergunta:")
    print(PERGUNTA_EXEMPLO)
    print("\nSaída estruturada (RespostaAgente):")
    print(f"categoria_risco: {resposta.categoria_risco}")
    print(f"recomendacao:    {resposta.recomendacao}")
    print(f"confianca:       {resposta.confianca:.2f}")


if __name__ == "__main__":
    main()
