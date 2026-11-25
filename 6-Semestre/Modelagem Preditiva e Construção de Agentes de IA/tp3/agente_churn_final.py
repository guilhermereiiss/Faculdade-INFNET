"""
Versão final do agente de análise de churn da NeoStream.

Integra os primitivos Agent e Runner do OpenAI Agents SDK, saída estruturada
em Pydantic (RespostaAgente) e execução assíncrona concorrente via asyncio.
"""

import asyncio
import os
import time

from agents import Agent, Runner, set_default_openai_api, set_tracing_disabled
from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator

INSTRUCOES_AGENTE_CHURN = """
Você é o agente de análise de risco de churn do time de retenção da NeoStream.
Sua missão é interpretar perguntas em linguagem natural sobre assinantes específicos,
avaliar o risco de cancelamento com base nos sinais comportamentais e comerciais fornecidos
e entregar uma recomendação estruturada pronta para o painel interno de retenção.

Diretrizes baseadas nos achados dos modelos de churn da NeoStream (TP1 e TP2):
1. Taxa base de churn da plataforma: ~17,6% dos assinantes.
2. Principais direcionadores aprendidos pela regressão logística (features padronizadas):
   - numero_reclamacoes (+0,31): principal fator de aumento do risco de cancelamento.
   - tempo_assinatura_meses (-0,48): principal fator protetor; assinantes novos cancelam mais.
   - uso_medio_semanal_horas (-0,20): menor engajamento eleva o risco de saída.
   - Variáveis categóricas (plano, método de pagamento, dispositivo) têm efeito secundário.
3. Assimetria de custo no negócio:
   - Falso negativo (perder o assinante sem agir) é mais caro do que falso positivo
     (oferecer uma ação de retenção preventiva).
   - Como o modelo estatístico de churn tem AUC moderada (~0,66), a recomendação deve
     combinar o score estimado (quando informado) com os sinais qualitativos do cliente.
4. Políticas comerciais disponíveis para retenção:
   - Contato proativo de suporte técnico/financeiro para zerar atritos de reclamações.
   - Oferta de pausa de até 30 dias ou downgrade de plano (Premium -> Padrão -> Básico).
   - Desconto direcionado para casos de risco alto, evitando descontos desnecessários em
     clientes fiéis de baixo risco.

Regras de saída (esquema RespostaAgente):
- categoria_risco: use estritamente "baixo", "medio" ou "alto".
- recomendacao: ação específica, proporcional ao perfil do assinante e aplicável pelo time.
- confianca: número decimal entre 0.0 e 1.0 refletindo a consistência e completude dos sinais.
""".strip()

PERGUNTAS_RETENCAO = [
    (
        "AST-10516 (plano Básico, cartão de crédito, Smart TV, 7,7 meses de assinatura, "
        "4,9 h/semana de uso, 3 reclamações registradas; probabilidade no modelo de churn: 51,3%): "
        "qual é a categoria de risco desse assinante e qual ação imediata de retenção devemos acionar?"
    ),
    (
        "AST-06809 (plano Premium, boleto, celular, apenas 1,2 mês de assinatura, 12,1 h/semana "
        "de uso, 0 reclamações; probabilidade no modelo de churn: 16,8%): por ser um cliente muito "
        "recente no boleto, vale oferecer desconto agora ou adotar outra abordagem?"
    ),
    (
        "AST-02841 (plano Padrão, cartão de crédito, tablet, 72,0 meses de assinatura, "
        "12,1 h/semana de uso, 0 reclamações; probabilidade no modelo de churn: 1,7%): "
        "esse assinante precisa entrar na campanha de desconto deste mês?"
    ),
    (
        "AST-00059 (plano Premium, boleto, Smart TV, 25,1 meses de assinatura, 10,3 h/semana "
        "de uso, mas acumulou 2 reclamações recentes): apesar do bom tempo de casa e uso regular, "
        "o histórico recente de reclamações exige intervenção do time de retenção?"
    ),
]


class RespostaAgente(BaseModel):
    categoria_risco: str = Field(
        description="Categoria de risco de churn: baixo, medio ou alto."
    )
    recomendacao: str = Field(
        description="Ação prática recomendada para o time de retenção da NeoStream."
    )
    confianca: float = Field(
        description="Grau de confiança da análise em escala decimal entre 0.0 e 1.0."
    )

    @field_validator("confianca")
    @classmethod
    def validar_intervalo_confianca(cls, valor: float) -> float:
        if not 0.0 <= valor <= 1.0:
            raise ValueError("confianca deve estar entre 0.0 e 1.0")
        return valor


def criar_agente_churn() -> Agent:
    modelo = os.getenv("OPENAI_DEFAULT_MODEL")
    return Agent(
        name="AgenteAnaliseChurnNeoStream",
        instructions=INSTRUCOES_AGENTE_CHURN,
        output_type=RespostaAgente,
        model=modelo,
    )


def validar_saida(resposta: object) -> RespostaAgente:
    if not isinstance(resposta, RespostaAgente):
        raise TypeError(f"Saída inesperada: {type(resposta).__name__}")
    return RespostaAgente.model_validate(resposta.model_dump())


async def analisar_assinante(agente: Agent, pergunta: str) -> tuple[RespostaAgente, float]:
    inicio = time.perf_counter()
    resultado = await Runner.run(agente, pergunta)
    duracao = time.perf_counter() - inicio
    resposta_validada = validar_saida(resultado.final_output)
    return resposta_validada, duracao


async def executar_demonstracao(perguntas: list[str]) -> None:
    agente = criar_agente_churn()
    inicio_total = time.perf_counter()
    resultados = await asyncio.gather(
        *(analisar_assinante(agente, pergunta) for pergunta in perguntas)
    )
    tempo_total = time.perf_counter() - inicio_total
    tempo_sequencial_estimado = sum(duracao for _, duracao in resultados)

    for indice, (pergunta, (resposta, duracao)) in enumerate(
        zip(perguntas, resultados), start=1
    ):
        print(f"=== Assinante {indice} ({duracao:.2f}s) ===")
        print(f"Pergunta:        {pergunta}")
        print(f"categoria_risco: {resposta.categoria_risco}")
        print(f"recomendacao:    {resposta.recomendacao}")
        print(f"confianca:       {resposta.confianca:.2f}")
        print()

    print("=== Resumo da execução final ===")
    print(f"Consultas concluídas e validadas: {len(resultados)}/{len(perguntas)}")
    print(f"Tempo total concorrente:          {tempo_total:.2f}s")
    print(f"Tempo sequencial estimado:        {tempo_sequencial_estimado:.2f}s")


def configurar_provedor() -> None:
    if os.getenv("OPENAI_BASE_URL"):
        set_default_openai_api("chat_completions")
        set_tracing_disabled(True)


def main() -> None:
    load_dotenv()
    configurar_provedor()
    asyncio.run(executar_demonstracao(PERGUNTAS_RETENCAO))


if __name__ == "__main__":
    main()
