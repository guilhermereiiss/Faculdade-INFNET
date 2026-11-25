# Justificativa de Design — Agente Final de Análise de Churn (`agente_churn_final.py`)

## 1. Visão geral da entrega final

O script `agente_churn_final.py` consolida as capacidades construídas ao longo dos Exercícios 1 a 7 em um componente único voltado à demonstração para o time de produto e à futura integração ao painel interno de retenção da NeoStream:

- **Definição declarativa do agente** via `Agent` e execução via `Runner` (OpenAI Agents SDK `0.26.0`);
- **Contrato de saída tipado e validado** com Pydantic (`output_type=RespostaAgente`);
- **Processamento assíncrono concorrente** com `async def`, `await Runner.run(...)`, `asyncio.gather(...)` e `asyncio.run(...)`;
- **Gestão segura de credenciais** por variáveis de ambiente (`.env` via `python-dotenv`, sem chaves no código ou no pacote de entrega).

---

## 2. Resultados observados na demonstração (4 assinantes da base NeoStream)

O agente final foi executado concorrentemente para quatro assinantes reais da base `assinantes_neostream.csv` (três deles analisados no TP2, acrescidos de um perfil de tensão intermediária):

| Assinante | Perfil resumido na pergunta | Latência | `categoria_risco` | `confianca` | Recomendação produzida |
|---|---|---|---|---|---|
| **AST-10516** | Básico, cartão, Smart TV, 7,7 meses, 4,9h/sem, 3 reclamações (prob. TP2: 51,3%) | `5,10 s` | `alto` | `0.95` | Realizar contato proativo imediato da equipe de suporte para resolver as 3 reclamações pendentes e oferecer um desconto temporário ou degustação de plano superior para reaproximar o cliente. |
| **AST-06809** | Premium, boleto, celular, 1,2 mês, 12,1h/sem, 0 reclamações (prob. TP2: 16,8%) | `5,12 s` | `baixo` | `0.90` | Não oferecer desconto agora, pois o cliente possui bom engajamento (12,1h/semana) e nenhuma reclamação. A melhor abordagem é incentivar a migração do boleto para cartão de crédito/débito automático para evitar inadimplência e reforçar as ações de onboarding. |
| **AST-02841** | Padrão, cartão, tablet, 72,0 meses, 12,1h/sem, 0 reclamações (prob. TP2: 1,7%) | `3,85 s` | `baixo` | `0.95` | Não incluir na campanha de desconto. O cliente possui longo tempo de assinatura (72 meses), zero reclamações e boa frequência de uso, apresentando risco de churn extremamente baixo (1,7%). Recomenda-se manter apenas ações de engajamento padrão para evitar concessão desnecessária de desconto. |
| **AST-00059** | Premium, boleto, Smart TV, 25,1 meses, 10,3h/sem, 2 reclamações recentes | `4,05 s` | `medio` | `0.85` | Realizar contato proativo de suporte especializado para tratar e resolver as 2 reclamações recentes, garantindo a satisfação do cliente sem necessidade de aplicar descontos imediatos, visto o alto tempo de assinatura e bom engajamento. |

- **Validação estrutural:** `4/4` respostas passaram integralmente na verificação `isinstance(..., RespostaAgente)` e `RespostaAgente.model_validate(...)`.
- **Desempenho assíncrono:** tempo total concorrente de **`5,13 s`** contra **`18,13 s`** de tempo sequencial estimado (soma das quatro latências individuais) — uma **redução de `71,7%`** no tempo total de espera (aceleração de `3,53×`).

---

## 3. Justificativa técnica de cada decisão de design

Cada escolha arquitetural responde a uma restrição concreta da operação de retenção da NeoStream, e não a preferência estética de implementação.

### 3.1 Uso dos primitivos `Agent` e `Runner` (OpenAI Agents SDK)

- **Por que é necessário na NeoStream:** o time de retenção envia perguntas abertas em linguagem natural misturando dados quantitativos (probabilidade do modelo do TP2, horas de uso, meses de casa), sinais de atrito (reclamações) e dúvidas comerciais (*"vale oferecer desconto agora?"*). Um script imperativo sobre chamadas HTTP cruas misturaria lógica de prompt, ciclo de execução, tratamento de retentativas e parsing de resposta no mesmo código.
- **O que a abstração resolve:** `Agent` separa de forma limpa a especificação de domínio (`instructions`, papel do analista de retenção, diretrizes aprendidas no TP1/TP2 e contrato `output_type`) da mecânica de execução gerenciada pelo `Runner` (gestão de turnos, retentativas automáticas em falhas transitórias, serialização de esquema e extração tipada de `final_output`).
- **Preparação para evolução:** adotar `Agent` + `Runner` agora viabiliza adicionar ferramentas reais (`tools`, como consulta direta ao banco de assinantes e chamada ao `pipeline_churn.joblib`) na próxima fase sem alterar a interface consumida pelo painel.

### 3.2 Saída estruturada com Pydantic (`output_type=RespostaAgente`)

- **Por que é necessário na NeoStream:** a saída do agente alimenta um **painel interno de retenção** que exibe indicadores padronizados (badge de categoria de risco, texto de recomendação e indicador de confiança) e pode disparar filas de atendimento conforme a criticidade. Se o agente respondesse em texto livre (como no Exercício 4), o backend precisaria de expressões regulares ou *parsing* ad hoc, sujeito a quebras sempre que a redação do LLM variasse.
- **O que a abstração resolve:** passar `output_type=RespostaAgente` ao `Agent` instrui o modelo a responder em conformidade estrita com o JSON Schema da classe Pydantic (`categoria_risco: str`, `recomendacao: str`, `confianca: float`), e o `Runner` desserializa e valida o retorno antes mesmo de entregá-lo ao código chamador. O validador adicional em `confianca` (`0.0 <= valor <= 1.0`) e a função `validar_saida(...)` asseguram integridade ponta a ponta para o painel.

### 3.3 Execução assíncrona (`Runner.run` + `asyncio.gather` + `asyncio.run`)

- **Por que é necessário na NeoStream:** no painel de retenção, múltiplos analistas consultam assinantes diferentes simultaneamente — além de lotes de avaliação rápida antes de campanhas. Como cada chamada ao LLM levou entre `3,85 s` e `5,12 s` de espera de rede (I/O), a execução síncrona (`Runner.run_sync`) enfileiraria todas as requisições: 4 consultas bloqueantes consumiriam `18,13 s`, travando a experiência do painel sob concorrência.
- **O que a abstração resolve:** reescrever a chamada em `async def` com `await Runner.run(...)` libera o *event loop* enquanto cada requisição aguarda a resposta da API. Com `asyncio.gather(...)`, as 4 análises foram concluídas em `5,13 s` (praticamente o tempo de uma única consulta), demonstrando que a arquitetura escala de forma não bloqueante para cargas reais do time de retenção.

### 3.4 Configuração segura via `.env` e `python-dotenv`

- **Por que é necessário na NeoStream:** credenciais de API expostas em código ou repositórios Git representam incidente direto de segurança e risco financeiro.
- **O que a prática resolve:** carregar `OPENAI_API_KEY` (e opcionalmente `OPENAI_BASE_URL` / `OPENAI_DEFAULT_MODEL`) via `.env` ignorado pelo Git e documentado por `.env.example` desacopla segredos do código-fonte e permite trocar ambientes (homologação, produção ou provedor compatível) sem editar uma única linha dos scripts.

---

## 4. Relação explícita entre o ciclo Perceber-Raciocinar-Agir (Exercício 1) e o agente final

No Exercício 1, projetamos o componente da NeoStream sobre o ciclo **Perceber → Raciocinar → Agir**, em contraste com o fluxo linear do script de classificação do TP1/TP2. Na execução real do `agente_churn_final.py`, cada etapa desse ciclo ficou observável nos resultados obtidos:

1. **Perceber (*Perceive*):**
   - Em vez de exigir um vetor fixo de 6 colunas como o `pipeline_churn.joblib`, o agente recebeu quatro perguntas com estruturas textuais e focos distintos: `AST-10516` pediu ação imediata diante de alta probabilidade (`51,3%`); `AST-06809` questionou o trade-off de dar desconto a um cliente recente no boleto; `AST-02841` perguntou se deveria entrar na campanha de desconto; e `AST-00059` nem sequer informou probabilidade numérica do modelo, apenas sinais comportamentais conflitantes (25,1 meses de casa e 10,3h/semana vs. 2 reclamações).
   - Junto com a pergunta do analista, o agente percebeu as diretrizes de negócio da NeoStream definidas em `INSTRUCOES_AGENTE_CHURN` (peso das reclamações, efeito protetor do tempo de casa/uso e custo assimétrico entre falso negativo e falso positivo).

2. **Raciocinar (*Reason*):**
   - **Ponderação de sinais convergentes (`AST-10516` e `AST-02841`):** quando todos os sinais apontaram na mesma direção, o agente classificou com alta confiança (`0.95`): risco `alto` para `AST-10516` (3 reclamações + uso baixo + 51,3% de churn) e risco `baixo` para `AST-02841` (72 meses + 12,1h/semana + 0 reclamações + 1,7% de churn).
   - **Deliberação sob sinais mistos (`AST-06809` e `AST-00059`):** aqui fica clara a superioridade frente a uma regra fixa ou a um mero `0`/`1`. Para `AST-06809` (cliente recente de 1,2 mês no boleto, porém com ótimo engajamento de 12,1h/semana e 0 reclamações), o agente evitou desperdiçar margem com desconto e recomendou onboarding + migração de pagamento (`confianca = 0.90`). Já para `AST-00059` (25,1 meses de fidelidade e bom uso, mas 2 reclamações recentes e sem probabilidade informada), o agente equilibrou os sinais opostos classificando como risco `medio`, reduziu adequadamente a confiança para `0.85` e indicou suporte especializado sem desconto imediato.

3. **Agir (*Act*):**
   - Para cada deliberação, o `Runner` materializou a decisão em uma ação operacional tipada: uma instância validada de `RespostaAgente` contendo categoria pronta para priorização visual no painel (`baixo`/`medio`/`alto`), recomendação específica ao contexto do assinante (suporte prioritário, onboarding/meio de pagamento, manutenção sem desconto ou oferta de retenção) e confiança numérica auditável (`0.85` a `0.95`), entregue concorrentemente em `5,13 s`.
   - Embora esta entrega valide o núcleo agêntico de turno único (*single-turn* sem ferramentas externas), a arquitetura sobre `Agent` e `Runner` já deixa o laço pronto para que, na próxima iteração, a etapa **Agir** inclua chamadas a ferramentas (consulta ao banco e ao `pipeline_churn.joblib`), realimentando o estágio **Perceber** com observações reais antes da resposta final.
