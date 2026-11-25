"""Execução assíncrona concorrente do agente estruturado da NeoStream com asyncio.gather."""

import asyncio
import time

from agents import Agent, Runner
from dotenv import load_dotenv

from agente_saida_estruturada import (
    RespostaAgente,
    configurar_provedor,
    criar_agente_estruturado,
)

PERGUNTAS_CONCORRENTES = [
    (
        "Assinante no plano Básico há 4 meses, assistindo apenas 2 horas por semana e com "
        "3 reclamações recentes no suporte. Qual o risco de churn e qual ação tomar?"
    ),
    (
        "Assinante no plano Padrão há 48 meses, uso médio de 14 horas por semana e zero "
        "reclamações, pagando no cartão de crédito. Qual o risco de churn e o que recomendar?"
    ),
]


async def consultar_agente(agente: Agent, pergunta: str) -> tuple[RespostaAgente, float]:
    inicio = time.perf_counter()
    resultado = await Runner.run(agente, pergunta)
    duracao = time.perf_counter() - inicio
    return resultado.final_output, duracao


async def executar_chamadas_concorrentes() -> None:
    agente = criar_agente_estruturado()

    inicio_total = time.perf_counter()
    resultados = await asyncio.gather(
        *(consultar_agente(agente, pergunta) for pergunta in PERGUNTAS_CONCORRENTES)
    )
    tempo_total_concorrente = time.perf_counter() - inicio_total
    tempo_sequencial_estimado = sum(duracao for _, duracao in resultados)

    for indice, (pergunta, (resposta, duracao)) in enumerate(
        zip(PERGUNTAS_CONCORRENTES, resultados), start=1
    ):
        print(f"=== Chamada {indice} ({duracao:.2f}s) ===")
        print(f"Pergunta:        {pergunta}")
        print(f"categoria_risco: {resposta.categoria_risco}")
        print(f"recomendacao:    {resposta.recomendacao}")
        print(f"confianca:       {resposta.confianca:.2f}")
        print()

    ganho_absoluto = tempo_sequencial_estimado - tempo_total_concorrente
    ganho_percentual = (
        (ganho_absoluto / tempo_sequencial_estimado) * 100
        if tempo_sequencial_estimado > 0
        else 0.0
    )

    print("=== Resumo de desempenho ===")
    print(f"Tempo total concorrente (asyncio.gather): {tempo_total_concorrente:.2f}s")
    print(f"Tempo sequencial estimado (soma):         {tempo_sequencial_estimado:.2f}s")
    print(f"Redução estimada:                         {ganho_absoluto:.2f}s ({ganho_percentual:.1f}%)")


def main() -> None:
    load_dotenv()
    configurar_provedor()
    asyncio.run(executar_chamadas_concorrentes())


if __name__ == "__main__":
    main()
