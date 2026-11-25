# Agente de IA vs. Chatbot Tradicional e Software Baseado em Regras

## 1. Resposta direta à pergunta do time de produto

O componente proposto para o time de retenção da NeoStream **não é apenas um chatbot com acesso ao modelo de churn**. Embora ambos possam interagir em linguagem natural, a diferença central está em **autonomia de decisão e orientação a objetivos**: enquanto um chatbot tradicional apenas responde turnos de conversa seguindo intenções pré-mapeadas ou um fluxo de diálogo, um agente de IA recebe um objetivo, decide autonomamente quais passos executar, combina múltiplas evidências (perfil do assinante, sinais de churn, políticas de retenção) e entrega uma decisão estruturada pronta para acionar processos do negócio.

Confundir os dois conceitos gera risco direto de escopo: esperar comportamento de agente de um chatbot leva a frustração por rigidez; construir um agente onde bastaria um chatbot aumenta custo de inferência, latência e complexidade de monitoramento sem retorno proporcional.

---

## 2. Características que diferenciam um Agente de IA

A tabela abaixo resume quatro propriedades estruturais que separam um agente de IA de um chatbot tradicional e de um software convencional baseado em regras (`if/else`):

| Característica | Software convencional baseado em regras | Chatbot tradicional (árvore/FAQ/intenções) | Agente de IA |
|---|---|---|---|
| **1. Autonomia na escolha de ações e ferramentas** | Executa somente ramificações explícitas escritas pelo programador; não decide novos caminhos diante de situações imprevistas. | Classifica a intenção da frase e dispara um fluxo ou resposta fixa associada àquela intenção. | Decide dinamicamente, em tempo de execução, quais passos ou ferramentas acionar e em que ordem para cumprir o objetivo. |
| **2. Raciocínio sobre entradas abertas e incompletas** | Falha ou cai em `default` quando um campo está ausente ou fora do padrão esperado. | Reconhece apenas variações próximas das intenções treinadas; perguntas compostas ou ambíguas quebram o fluxo. | Interpreta perguntas abertas em linguagem natural, sintetiza múltiplos sinais parciais e pondera incerteza (ex.: ajustando `confianca`). |
| **3. Execução iterativa orientada a objetivo (loop)** | Fluxo único (*input → regra → output*), sem reavaliação baseada no resultado intermediário. | Interação reativa turno a turno (*pergunta → resposta*), sem planejamento multi-etapas. | Opera em ciclo perceber-raciocinar-agir: avalia cada resultado parcial e continua até satisfazer o critério de conclusão. |
| **4. Integração entre linguagem natural e saída operacional estruturada** | Saída tipada e rígida, mas sem compreensão semântica de entrada livre. | Saída majoritariamente em texto conversacional voltado a leitura humana. | Compreende entrada livre e produz tanto justificativa contextualizada quanto contratos tipados (ex.: Pydantic) para sistemas internos. |

---

## 3. Por que o componente de análise de churn da NeoStream deve ser um Agente

No contexto da NeoStream, o analista de retenção não faz perguntas padronizadas de resposta única. Ele traz cenários heterogêneos que combinam comportamento de consumo, histórico de atrito e restrições comerciais:

- **Perguntas compostas e não padronizadas:** um analista pode perguntar *"Assinante no plano básico há 2 meses, assistindo menos de 2h por semana e com 3 reclamações no boleto: qual o risco e o que ofereço sem queimar margem?"*. Um software baseado em regras exigiria uma matriz combinatória frágil de `if/else` para cobrir todas as interações entre plano, tempo de casa, uso, reclamações e orçamento; um chatbot de FAQ não conseguiria cruzar esses sinais para sintetizar uma recomendação coerente.
- **Ponderação do tradeoff de negócio do TP2:** no TP2 ficou claro que o modelo de `LogisticRegression` tem AUC-ROC moderado (`0,6640`) e que o threshold padrão (`0.5`) gera recall de apenas `0,5%`, deixando passar quase todos os cancelamentos. A decisão operacional depende de equilibrar o alto custo do falso negativo com o orçamento de descontos. Um agente consegue raciocinar sobre esse tradeoff ao classificar a categoria de risco (`alto`, `medio`, `baixo`), calibrar a confiança da análise e sugerir ações proporcionais (desde contato proativo de suporte até oferta de retenção).
- **Consumo direto pelo painel interno:** além de interpretar a pergunta em linguagem natural, o componente precisa devolver dados validados (`categoria_risco`, `recomendacao`, `confianca`) de forma assíncrona para alimentar o painel do time de retenção em tempo real, papel que um chatbot puramente conversacional não atende por design.
- **Evolução incremental para ferramentas reais:** projetar o componente desde já sobre a arquitetura de agente (`Agent` + `Runner`) permite plugar, nas próximas entregas, ferramentas como consulta ao banco de assinantes, chamada direta ao `pipeline_churn.joblib` e consulta às campanhas de desconto ativas, sem reescrever o núcleo do produto.

---

## 4. Quando um chatbot simples seria suficiente (e um agente não se justificaria)

Nem toda demanda conversacional na NeoStream pede um agente de IA. Um caso de uso claro em que um **chatbot simples** (ou até uma busca estruturada em base de conhecimento / árvore de decisão) é a escolha mais adequada:

- **Atendimento de autoatendimento para dúvidas fixas do assinante no aplicativo:** por exemplo, responder perguntas recorrentes e fechadas como *"Como alterar meu cartão de crédito?"*, *"Onde encontro o botão para cancelar minha assinatura?"*, *"Qual o preço do plano Padrão?"* ou *"Até quando mantenho acesso após cancelar?"*.

**Por que não usar um agente nesse cenário:**
1. **Respostas determinísticas e reguladas:** o texto da política de cobrança e cancelamento não deve variar nem ser "criativamente" reinterpretado a cada requisição; erros de interpretação podem gerar passivo de atendimento (PROCON/CDC).
2. **Sem necessidade de planejamento ou composição:** cada pergunta mapeia diretamente para um artigo ou fluxo estático de 1 passo.
3. **Custo, latência e previsibilidade:** um chatbot baseado em intents/FAQ ou busca simples responde em milissegundos, com custo marginal próximo de zero e risco nulo de alucinação, evitando a sobrecarga de orquestração e o custo por token de um agente de IA.
