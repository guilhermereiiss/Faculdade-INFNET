# Validação Programática de Saída Estruturada Assíncrona

Registro da execução do script consolidado `agente_estruturado_assincrono.py`, que combina saída estruturada em Pydantic (`output_type=RespostaAgente`) com execução assíncrona concorrente (`Runner.run` + `asyncio.gather` + `asyncio.run`) para três consultas distintas sobre risco de churn.

---

## 1. Critérios de validação programática aplicados

Cada um dos três objetos retornados em `resultado.final_output` passou pela função `validar_resposta_pydantic(...)`, que verifica automaticamente:

1. **Instância Pydantic:** `isinstance(objeto, RespostaAgente)` é `True`.
2. **Presença exata de campos:** `set(objeto.model_dump().keys()) == {"categoria_risco", "recomendacao", "confianca"}` (nenhum campo ausente ou extra).
3. **Revalidação completa pelo esquema Pydantic:** `RespostaAgente.model_validate(dados)` executa sem lançar `ValidationError`.
4. **Verificação estrita de tipos e domínio:**
   - `categoria_risco`: `str` não vazia;
   - `recomendacao`: `str` não vazia;
   - `confianca`: `float` (rejeitando `bool`) dentro do intervalo `[0.0, 1.0]`.

---

## 2. Resultados coletados e validados (3 consultas concorrentes)

- **Tempo total concorrente (`asyncio.gather`):** `4,38 s` *(vs. `11,45 s` sequencial estimado: `4,38 s + 4,15 s + 2,92 s`)*
- **Taxa de aprovação na validação:** **`3/3` objetos válidos (`100%`)**

| # | Perfil consultado | Latência | `categoria_risco` (`str`) | `confianca` (`float`) | `recomendacao` (`str`) | Status da validação |
|---|---|---|---|---|---|---|
| 1 | Plano Básico, 2 meses, 1,5h/sem, boleto, 4 reclamações no último mês | `4,38 s` | `alto` | `0.95` | Priorizar contato imediato com o cliente para resolver pontualmente as 4 reclamações abertas, oferecendo suporte dedicado e uma oferta de retenção para reengajamento. | **Válido** (`RespostaAgente`) |
| 2 | Plano Premium, 6 meses, 8h/sem no celular, 1 reclamação recente sobre travamento no app | `4,15 s` | `medio` | `0.85` | Acionar o suporte técnico prioritário para resolver a falha de travamento no aplicativo e oferecer um benefício compensatório na assinatura para garantir a satisfação do cliente. | **Válido** (`RespostaAgente`) |
| 3 | Plano Padrão, 54 meses, 15h/sem na Smart TV, cartão de crédito, 0 reclamações | `2,92 s` | `baixo` | `0.95` | Manter o engajamento com comunicações sobre lançamentos do catálogo e oferecer um benefício pontual de fidelidade pelo longo tempo de assinatura. | **Válido** (`RespostaAgente`) |

---

## 3. Evidência da verificação de tipos por objeto

Em todas as três consultas, o relatório retornado por `validar_resposta_pydantic` confirmou conformidade integral com o contrato `RespostaAgente`:

```python
{
    "tipo_instancia": "RespostaAgente",
    "campos_presentes": ["categoria_risco", "confianca", "recomendacao"],
    "tipos": {
        "categoria_risco": "str",
        "recomendacao": "str",
        "confianca": "float",
    },
    "valido": True,
}
```

---

## 4. Conclusão da validação

- Nenhum objeto apresentou campo ausente, tipo incorreto ou valor de confiança fora de `[0.0, 1.0]`.
- As categorias e níveis de confiança refletiram coerência com os sinais de negócio da NeoStream: o caso ambíguo (plano Premium com uso bom de 8h/semana, mas 1 reclamação técnica) recebeu risco `medio` e confiança menor (`0.85`), enquanto os dois extremos receberam `alto` e `baixo` com confiança `0.95`.
- A consolidação garante que o painel interno de retenção pode consumir os três campos diretamente (`resposta.categoria_risco`, `resposta.recomendacao`, `resposta.confianca`) sem *parsing* frágil de texto livre e sem bloquear solicitações simultâneas.
