# Execução Assíncrona e Concorrência — `Runner.run` + `asyncio.gather`

Registro da execução concorrente do agente estruturado (`RespostaAgente`) usando `Runner.run(...)` em função `async def`, disparado via `asyncio.run(...)` e paralelizado com `asyncio.gather(...)` no script `agente_assincrono.py`.

---

## 1. Cenário testado

Duas requisições simultâneas foram enviadas ao agente de retenção da NeoStream para simular analistas consultando o painel interno ao mesmo tempo:

| Chamada | Perfil consultado | `categoria_risco` | `confianca` | Latência individual |
|---|---|---|---|---|
| **Chamada 1** | Plano Básico, 4 meses, 2h/semana, 3 reclamações recentes no suporte | `alto` | `0.95` | `3,74 s` |
| **Chamada 2** | Plano Padrão, 48 meses, 14h/semana, 0 reclamações, cartão de crédito | `baixo` | `0.95` | `2,93 s` |

### Recomendações retornadas

- **Chamada 1:** *"Realizar contato proativo e prioritário do suporte para solucionar as 3 reclamações e oferecer um incentivo de retenção, como um desconto temporário ou pausa de assinatura."*
- **Chamada 2:** *"Manter engajamento ativo com recomendações personalizadas de conteúdo e reconhecer a fidelidade do cliente, sem necessidade de conceder descontos agressivos."*

---

## 2. Comparação de tempo: concorrente vs. sequencial estimado

| Métrica | Valor observado | Como foi obtido |
|---|---|---|
| Tempo individual — Chamada 1 | `3,74 s` | `time.perf_counter()` em torno de `await Runner.run(...)` |
| Tempo individual — Chamada 2 | `2,93 s` | `time.perf_counter()` em torno de `await Runner.run(...)` |
| **Tempo total concorrente (`asyncio.gather`)** | **`3,74 s`** | Tempo total de relógio do `asyncio.gather(...)` |
| **Tempo sequencial estimado** | **`6,67 s`** | Soma dos tempos individuais (`3,74 s + 2,93 s`) |
| **Ganho obtido com concorrência** | **`-2,93 s` (`43,9%` mais rápido)** | Redução proporcionada pela sobreposição de espera de rede (I/O) |

---

## 3. Análise técnica para o painel de retenção

- Chamadas a LLMs são operações predominantemente **I/O-bound**: quase todo o tempo de resposta é gasto aguardando o retorno HTTP da API externa, não consumindo CPU local.
- Com `Runner.run_sync(...)`, a segunda consulta só iniciaria após o término completo da primeira (`~6,67 s` no total), bloqueando o *event loop* ou o servidor do painel interno enquanto a requisição anterior aguarda resposta.
- Com `await Runner.run(...)` combinado a `asyncio.gather(...)`, as duas requisições ficam em trânsito simultaneamente; o tempo total aproxima-se do tempo da chamada mais lenta (`max(3,74 s, 2,93 s) = 3,74 s`), garantindo responsividade para múltiplos analistas consultando o painel em tempo real.
