"""Consolidação do agente com saída estruturada Pydantic e execução assíncrona validada."""

import asyncio
import os
import time

from agents import Agent, Runner, set_default_openai_api, set_tracing_disabled
from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator

INSTRUCOES_AGENTE = """
Você é o agente especialista de análise de risco de churn da NeoStream.
Avalie o perfil descrito pelo time de retenção e produza uma resposta estruturada confiável
para exibição no painel interno.

Sinais de risco da base NeoStream:
- Mais reclamações elevam significativamente a probabilidade de cancelamento.
- Maior tempo de assinatura (meses) e maior uso semanal (horas) reduzem o risco de churn.
- Deixar um assinante em risco cancelar (falso negativo) custa mais caro do que agir preventivamente.

Preencha os campos da resposta seguindo estritamente:
- categoria_risco: "baixo", "medio" ou "alto".
- recomendacao: ação objetiva e aplicável pelo time de retenção.
- confianca: valor decimal entre 0.0 e 1.0 coerente com a clareza dos sinais fornecidos.
""".strip()

PERGUNTAS_CHURN = [
    (
        "Cliente no plano Básico há 2 meses, assistindo 1,5 hora por semana, pagando por boleto "
        "e com 4 reclamações abertas no último mês. Qual o risco de cancelamento e a ação indicada?"
    ),
    (
        "Cliente no plano Premium há 6 meses, uso médio de 8 horas por semana no celular, "
        "1 reclamação recente sobre travamento no app. Qual o nível de risco e o que devemos fazer?"
    ),
    (
        "Cliente no plano Padrão há 54 meses, uso estável de 15 horas por semana na Smart TV, "
        "pagamento em cartão de crédito e nenhuma reclamação. Há risco de churn?"
    ),
]

CAMPOS_ESPERADOS = {"categoria_risco", "recomendacao", "confianca"}


class RespostaAgente(BaseModel):
    categoria_risco: str = Field(
        description="Categoria de risco de churn do assinante: baixo, medio ou alto."
    )
    recomendacao: str = Field(
        description="Ação prática recomendada para o time de retenção."
    )
    confianca: float = Field(
        description="Confiança da análise em escala decimal entre 0.0 e 1.0."
    )

    @field_validator("confianca")
    @classmethod
    def validar_intervalo_confianca(cls, valor: float) -> float:
        if not 0.0 <= valor <= 1.0:
            raise ValueError("confianca deve estar entre 0.0 e 1.0")
        return valor


def criar_agente() -> Agent:
    modelo = os.getenv("OPENAI_DEFAULT_MODEL")
    return Agent(
        name="AgenteEstruturadoAssincronoNeoStream",
        instructions=INSTRUCOES_AGENTE,
        output_type=RespostaAgente,
        model=modelo,
    )


def validar_resposta_pydantic(objeto: object) -> dict[str, object]:
    if not isinstance(objeto, RespostaAgente):
        raise TypeError(f"Esperado RespostaAgente, recebido {type(objeto).__name__}")

    dados = objeto.model_dump()
    if set(dados.keys()) != CAMPOS_ESPERADOS:
        raise ValueError(f"Campos divergentes: {set(dados.keys())} != {CAMPOS_ESPERADOS}")

    revalidado = RespostaAgente.model_validate(dados)

    if not isinstance(revalidado.categoria_risco, str) or not revalidado.categoria_risco.strip():
        raise ValueError("categoria_risco deve ser string não vazia")
    if not isinstance(revalidado.recomendacao, str) or not revalidado.recomendacao.strip():
        raise ValueError("recomendacao deve ser string não vazia")
    if isinstance(revalidado.confianca, bool) or not isinstance(revalidado.confianca, float):
        raise TypeError("confianca deve ser float")
    if not 0.0 <= revalidado.confianca <= 1.0:
        raise ValueError("confianca fora do intervalo [0.0, 1.0]")

    return {
        "tipo_instancia": type(objeto).__name__,
        "campos_presentes": sorted(dados.keys()),
        "tipos": {campo: type(valor).__name__ for campo, valor in dados.items()},
        "valido": True,
    }


async def executar_consulta(agente: Agent, pergunta: str) -> tuple[RespostaAgente, float]:
    inicio = time.perf_counter()
    resultado = await Runner.run(agente, pergunta)
    return resultado.final_output, time.perf_counter() - inicio


async def executar_e_validar() -> None:
    agente = criar_agente()
    inicio_total = time.perf_counter()
    execucoes = await asyncio.gather(
        *(executar_consulta(agente, pergunta) for pergunta in PERGUNTAS_CHURN)
    )
    tempo_total = time.perf_counter() - inicio_total

    respostas: list[RespostaAgente] = []
    for indice, (pergunta, (resposta, duracao)) in enumerate(
        zip(PERGUNTAS_CHURN, execucoes), start=1
    ):
        relatorio = validar_resposta_pydantic(resposta)
        respostas.append(resposta)

        print(f"=== Consulta {indice} ({duracao:.2f}s) ===")
        print(f"Pergunta:        {pergunta}")
        print(f"categoria_risco: {resposta.categoria_risco}")
        print(f"recomendacao:    {resposta.recomendacao}")
        print(f"confianca:       {resposta.confianca:.2f}")
        print(f"Validação:       {relatorio}")
        print()

    print(
        f"Total validado com sucesso: {len(respostas)}/{len(PERGUNTAS_CHURN)} objetos "
        f"RespostaAgente em {tempo_total:.2f}s."
    )


def configurar_provedor() -> None:
    if os.getenv("OPENAI_BASE_URL"):
        set_default_openai_api("chat_completions")
        set_tracing_disabled(True)


def main() -> None:
    load_dotenv()
    configurar_provedor()
    asyncio.run(executar_e_validar())


if __name__ == "__main__":
    main()
