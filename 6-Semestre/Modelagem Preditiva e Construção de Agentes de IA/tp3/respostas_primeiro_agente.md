# Respostas do Primeiro Agente — Política de Cancelamento NeoStream

Registro da execução síncrona (`Runner.run_sync`) do script `primeiro_agente.py`, que valida o fluxo mínimo de criação e execução de um `Agent` do OpenAI Agents SDK (`openai-agents==0.26.0`), sem ferramentas externas, configurado apenas com `instructions` de política de cancelamento da NeoStream.

- **Script executado:** `primeiro_agente.py`
- **Primitivos utilizados:** `Agent(name=..., instructions=...)` e `Runner.run_sync(agente, pergunta)`
- **Modelo utilizado na execução local:** `gemini-3.6-flash` (via endpoint compatível configurado em `.env`)

---

## Pergunta 1

> Se eu cancelar minha assinatura hoje no meio do mês, perco o acesso imediatamente ou continuo assistindo até o fim do período já pago? Existe alguma multa de fidelidade?

### Resposta obtida

> Olá! Na NeoStream, **você não perde o acesso imediatamente**.
>
> Ao cancelar a sua assinatura no meio do mês, o seu acesso permanecerá ativo normalmente até o final do ciclo de cobrança que já foi pago. Após esse período, o acesso é encerrado e não haverá nenhuma cobrança no ciclo seguinte.
>
> Além disso, **não existe nenhuma multa de fidelidade**. Não exigimos contrato de fidelidade e não cobramos nenhuma taxa de rescisão, ou seja, você pode cancelar a qualquer momento sem nenhum custo adicional.
>
> Se precisar de mais alguma informação ou quiser conhecer opções como a pausa da assinatura por até 30 dias ou a troca de plano, estou à disposição!

---

## Pergunta 2

> Contratei o plano Premium há 4 dias pagando com PIX e decidi não continuar. Tenho direito a reembolso integral ou existe alguma alternativa como reduzir meu plano?

### Resposta obtida

> Olá! Que bom falar com você.
>
> **Sim, você tem direito ao reembolso integral!**
>
> Como a contratação foi feita há 4 dias, você está dentro do prazo de 7 dias corridos (direito de arrependimento para a primeira contratação). Esse reembolso total é garantido independentemente do meio de pagamento, incluindo o PIX.
>
> Além disso, caso prefira continuar na NeoStream, temos **alternativas ao cancelamento**:
> 1. **Downgrade de plano:** Você pode alterar seu plano do Premium para o **Padrão** ou **Básico** antes do próximo ciclo.
> 2. **Pausar assinatura:** Você pode pausar sua assinatura por até 30 dias.
>
> Vale lembrar que na NeoStream **não há fidelidade nem taxa de rescisão/multa**. Você pode escolher solicitar o cancelamento com reembolso imediato ou optar por mudar para um plano mais em conta.
>
> Se precisar de ajuda para realizar qualquer um desses procedimentos, estou à disposição!

---

## Observações sobre a prova de conceito

- Nas duas perguntas, o agente respeitou estritamente as cinco regras definidas em `instructions` (ausência de multa/fidelidade, acesso até o fim do ciclo pago, reembolso integral em até 7 dias corridos mesmo via PIX e alternativas de pausa/downgrade).
- Embora a resposta em texto livre seja clara para leitura humana, ela não tem esquema fixo nem campos validáveis por código — motivação direta para o Exercício 5 (`output_type=RespostaAgente` em Pydantic).
