# Arquitetura do Agente de Retenção: Ciclo Perceber-Raciocinar-Agir

## 1. Contexto na NeoStream

No TP1 e no TP2, entregamos um pipeline de classificação supervisionada (`pipeline_churn.joblib`, baseado em `LogisticRegression` com `C = 0.01`, AUC-ROC de `0,6640` no conjunto de teste) que recebe os atributos tabulares de um assinante — tempo de assinatura, uso semanal, número de reclamações, plano, método de pagamento e dispositivo principal — e devolve uma probabilidade de cancelamento ou um rótulo binário (`0` ou `1`).

Esse artefato resolve bem a pontuação em lote (*batch scoring*), mas exige que um humano interprete o número isolado, cruze o score com o histórico do cliente, consulte regras de política comercial e decida qual abordagem de retenção aplicar. O próximo passo pedido pelo time de retenção é um **componente agêntico** que receba perguntas em linguagem natural (por exemplo, *"O assinante AST-10516 tem risco real de cancelar este mês? Que oferta faz sentido para ele?"*) e conduza autonomamente a investigação até entregar uma recomendação fundamentada.

---

## 2. Ciclo Perceber → Raciocinar → Agir no cenário de retenção

Um agente de IA opera em um laço iterativo orientado a objetivos, e não em uma passagem única de código:

```
   ┌──────────────────────────────────────────────────────────────┐
   │                                                              │
   ▼                                                              │
[PERCEBER]  ──►  [RACIOCINAR]  ──►  [AGIR]  ──►  (Objetivo atingido?)
 Pergunta,       Interpreta intenção,   Consulta ferramentas /     │ Não: novo ciclo
 contexto e      planeja passos,        chama modelo de churn /    │ com nova observação
 observações     avalia evidências      gera saída estruturada     │
                                                                   ▼ Sim: resposta final
```

### 2.1 Perceber (*Perceive*)
O componente capta entradas heterogêneas e não estruturadas, além das observações retornadas por suas próprias ações anteriores:
- **Entrada inicial do analista:** pergunta em linguagem natural com nível variável de detalhamento (pode trazer um `cliente_id`, um perfil resumido como *"plano básico, 3 reclamações e 2h/semana"*, ou uma dúvida de política de cancelamento).
- **Contexto do sistema:** instruções de papel (*system instructions*), regras de negócio da NeoStream (como a assimetria de custo entre falso negativo e falso positivo analisada no TP2) e o contrato de saída esperado (ex.: esquema Pydantic com categoria de risco, recomendação e confiança).
- **Observações intermediárias (em ciclos com ferramentas):** retorno da consulta à base de assinantes, score do modelo `pipeline_churn.joblib`, histórico de reclamações ou cláusulas da política comercial.

### 2.2 Raciocinar (*Reason*)
Com base no que percebeu, o modelo de linguagem (LLM) delibera dinamicamente antes de responder ou chamar outra ação:
- **Interpretação de intenção:** identifica se a solicitação pede análise de risco individual, enquadramento em política de cancelamento ou recomendação de ação de retenção.
- **Planejamento e decisão de suficiência:** avalia quais dados faltam para embasar a resposta (por exemplo, se precisa do score de churn e do histórico de uso antes de sugerir desconto) e qual é o nível de risco compatível com os sinais presentes (no modelo do TP2, maior número de reclamações eleva fortemente o logit de churn, enquanto maior tempo de casa e maior uso semanal o reduzem).
- **Ponderação de negócio:** considera o tradeoff precisão × recall documentado no TP2 — em que deixar um cliente cancelar (falso negativo) custa mais do que oferecer um incentivo conservador — e calibra o grau de confiança conforme a completude das informações recebidas.

### 2.3 Agir (*Act*)
A decisão do estágio de raciocínio se materializa em ações concretas:
- **Ações intermediárias (quando equipado com ferramentas):** invocar consultas de perfil, executar o pipeline de churn ou buscar regras de retenção; cada retorno volta ao estágio **Perceber** para refinar o raciocínio.
- **Ação final:** produzir uma resposta fundamentada — em linguagem natural ou em um objeto estruturado e validado (como `RespostaAgente` em Pydantic) — pronta para ser consumida pelo analista ou renderizada diretamente no painel interno de retenção.

---

## 3. Agente (ciclo perceber-raciocinar-agir) vs. Script tradicional (fluxo linear)

O script `pipeline_final_churn.py` do TP1/TP2 segue o modelo clássico de processamento linear:

```
Entrada fixa (DataFrame com 6 features) ──► pipeline.predict_proba(X) ──► Saída fixa (0/1 ou float)
```

A tabela abaixo contrasta as duas abordagens:

| Dimensão | Script tradicional (`pipeline_final_churn.py`) | Componente agêntico (ciclo perceber-raciocinar-agir) |
|---|---|---|
| **Fluxo de controle** | Estático e determinístico: a sequência de chamadas é codificada pelo desenvolvedor em tempo de projeto. | Dinâmico e orientado a objetivo: o próprio agente decide em tempo de execução o que investigar, em que ordem e quando encerrar o ciclo. |
| **Contrato de entrada** | Rígido e tabular: exige exatamente as colunas esperadas (`tempo_assinatura_meses`, `uso_medio_semanal_horas`, etc.); entradas fora do formato causam erro ou exigem pré-processamento manual. | Flexível e semântico: aceita perguntas em linguagem natural com formulações variadas, sinais incompletos e objetivos compostos. |
| **Capacidade de composição e justificativa** | Retorna apenas um valor numérico ou classe (`0`/`1`), sem explicar a decisão nem adaptá-la a regras de retenção. | Combina sinais de risco com diretrizes de negócio, produz recomendação acionável e explicita a confiança da análise. |
| **Tratamento de incerteza** | Aplica sempre a mesma fórmula matemática e o mesmo threshold fixo. | Avalia se há contexto suficiente, ajusta a confiança reportada e adapta a recomendação ao cenário descrito. |

### Diferenças arquiteturais concretas em destaque

1. **Controle de fluxo em tempo de execução vs. tempo de compilação/código:** no script tradicional, o grafo de execução é fixo (`dividir_dados` → `ColumnTransformer` → `LogisticRegression` → `predict`). No agente, o fluxo é um **loop de decisão** comandado pelo motor de raciocínio (LLM) dentro de um runtime (`Runner`), capaz de adaptar a trajetória conforme a pergunta recebida e as observações obtidas a cada passo.
2. **Fronteira semântica de entrada/saída vs. contrato estritamente posicional/tabular:** o script tradicional opera exclusivamente sobre vetores numéricos e categorias previamente codificadas, devolvendo escalares. A arquitetura agêntica introduz uma camada de compreensão semântica na entrada (linguagem natural) acoplada a uma camada de **validação estruturada na saída** (ex.: Pydantic), permitindo traduzir perguntas humanas arbitrárias em recomendações tipadas que sistemas downstream (como o painel de retenção) conseguem consumir com segurança.
3. **Separação entre previsão estatística e tomada de decisão operacional:** o modelo de ML (`LogisticRegression`) estima uma probabilidade a partir de padrões históricos, mas não "sabe" o que fazer com ela. Na arquitetura agêntica, o modelo preditivo passa a ser uma fonte de evidência (um sinal), enquanto o agente assume o papel de orquestrar contexto, política de cancelamento e recomendação de ação.
