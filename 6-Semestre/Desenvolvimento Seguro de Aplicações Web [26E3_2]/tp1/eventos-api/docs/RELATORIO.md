# Relatório técnico — eventos-api

> **Disciplina:** Programação Distribuída e Redes com Linux e Python  
> **Turma:** 26E1_5 — Instituto Infnet  
> **Professor:** Ricardo Pires  
> **Aluno:** Guilherme Reis

---

## Visão geral

Este relatório documenta as decisões técnicas tomadas na construção do `eventos-api`, API REST em FastAPI, ao longo dos 8 exercícios do TP de Ambiente Seguro em Programação. O código-fonte completo, organizado nos módulos `routes`, `models` e `database` (Exercício 4), acompanha este relatório no arquivo `.zip` da entrega.

---

## Exercício 1 — Ambiente e primeira rota

**Decisão:** ambiente virtual criado com `venv` (equivalente ao `virtualenv` pedido, nativo do Python 3), isolando as dependências do projeto do restante do sistema. Dependências (`fastapi`, `uvicorn`) registradas em `requirements.txt` via `pip freeze`.

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn[standard] jinja2 python-multipart
pip freeze > requirements.txt
uvicorn main:app --reload
```

**Evidência — servidor no ar e rota `GET /` respondendo:**

```
$ curl http://127.0.0.1:8000/
{"status":"ok","servico":"eventos-api","versao":"0.1.0"}
```

---

## Exercício 2 — Estrutura modular com APIRouter

**Decisão:** as rotas do recurso eventos foram isoladas em `routes/eventos.py`, usando `APIRouter(prefix="/eventos")` e registradas em `main.py` via `include_router`. O `main.py` não conhece nenhum detalhe de implementação do domínio eventos.

Foram implementadas quatro operações RESTful:

| Método | Rota | Operação |
|---|---|---|
| `GET` | `/eventos/` | Listar todos os eventos |
| `POST` | `/eventos/` | Criar novo evento |
| `GET` | `/eventos/{id}` | Obter evento por ID |
| `DELETE` | `/eventos/{id}` | Remover evento |

**Justificativa:** separar routers por recurso evita que uma mudança em um domínio quebre silenciosamente outro por estarem no mesmo arquivo — problema descrito no enunciado (rota de pagamentos afetando notificações). Cada `APIRouter` isola as rotas de um recurso; um novo desenvolvedor sabe exatamente onde adicionar um novo domínio (criar um novo arquivo + `include_router`) sem tocar em código existente.

**Evidência:**

```
$ curl http://127.0.0.1:8000/eventos/1
{"id":1,"nome":"PythonBrasil 2025","data":"2025-10-15","organizador":"Ana Lima","local":"São Paulo"}

$ curl http://127.0.0.1:8000/eventos/
[{"id":1,"nome":"PythonBrasil 2025",...},{"id":2,"nome":"FastAPI Meetup RJ",...}]
```

---

## Exercício 3 — Controle de exposição de dados com response_model

**Decisão:** dois schemas Pydantic distintos — `EventoResponse` (id, nome, data, organizador, local, descrição) e `EventoInterno` (herda de `EventoCreate` e adiciona `organizador_id` e `token_auditoria`). O endpoint de criação usa `response_model=EventoResponse`, e um endpoint adicional (`POST /eventos/inseguro/criar`) foi criado **apenas para fins de comparação**, sem `response_model`, para demonstrar o vazamento.

**Comparação das respostas JSON** (mesmo payload de entrada em ambos):

Com `response_model=EventoResponse`:
```
$ curl -X POST http://127.0.0.1:8000/eventos/ \
  -H "Content-Type: application/json" \
  -d '{"nome":"PythonBrasil","data":"2025-10-15","organizador":"Ana Lima","local":"SP"}'

{"id":1,"nome":"PythonBrasil","data":"2025-10-15","organizador":"Ana Lima","local":"SP","descricao":null}
```

Sem `response_model` (`/eventos/inseguro/criar`):
```
{"id":2,"nome":"PythonBrasil","data":"2025-10-15","organizador":"Ana Lima","local":"SP",
 "descricao":null,"organizador_id":"ORG-0002","token_auditoria":"3f7a1b2c-ecbe-4986-a9ea-0cabc00fe7a1"}
```

**Dado sensível exposto e impacto:** sem `response_model`, a rota expõe `organizador_id` (identificador interno sequencial) e `token_auditoria` (token interno de rastreamento). Na prática, isso permite que qualquer cliente colete IDs sequenciais de organizadores criando vários eventos, abrindo caminho para ataques de enumeração ou uso indevido do token de auditoria em chamadas internas que confiem nele.

---

## Exercício 4 — Reorganização em módulos

**Decisão:** o projeto foi reorganizado em três módulos:

```
eventos-api/
├── main.py                 # Bootstrap; apenas cria o app e registra routers
├── routes/
│   └── eventos.py          # Rotas HTTP do recurso eventos (JSON + HTML)
├── models/
│   └── evento.py           # Schemas Pydantic: EventoCreate, EventoInterno, EventoResponse
├── database/
│   └── db.py               # Acesso a dados em memória + funções CRUD + seeds
└── templates/
    ├── base.html            # Template base com cabeçalho e rodapé
    └── eventos/
        ├── lista.html       # Herda base.html
        └── detalhe.html     # Herda base.html
```

| Módulo | Responsabilidade |
|---|---|
| `main.py` | Inicializa o app, registra routers e hooks de lifecycle. Sem rotas de domínio. |
| `routes/` | Rotas HTTP por recurso. Um arquivo por domínio. |
| `models/` | Contratos Pydantic de entrada e saída. Controla o que a API expõe. |
| `database/` | Acesso e manipulação de dados. Hoje em memória; trocável por ORM sem mexer nas rotas. |
| `templates/` | Templates Jinja2 para renderização HTML server-side. |

Todas as rotas dos exercícios anteriores foram testadas novamente após a reorganização e permaneceram funcionais.

---

## Exercício 5 — Página HTML com Jinja2

**Decisão:** `Jinja2Templates` integrado no router de eventos com `directory="templates"`, reaproveitando diretamente `database/db.py` — a mesma fonte de dados usada pela rota JSON — sem duplicar lógica de acesso. Duas rotas HTML foram adicionadas:

```
GET /eventos/html/lista   →  templates/eventos/lista.html
GET /eventos/html/{id}    →  templates/eventos/detalhe.html
```

Cada página exibe pelo menos três campos por evento: **nome**, **data** e **organizador** (mais local e descrição).

**Evidência — rota JSON original continua funcionando sem interferência:**

```
$ curl http://127.0.0.1:8000/eventos/
[{"id":1,"nome":"PythonBrasil 2025",...},{"id":2,"nome":"FastAPI Meetup RJ",...}]
```

---

## Exercício 6 — XSS e herança de templates

**Reprodução do relatado pelo QA** — evento cadastrado com `<script>` no nome:

```
$ curl -X POST http://127.0.0.1:8000/eventos/ \
  -H "Content-Type: application/json" \
  -d '{"nome":"<script>alert(1)</script>","data":"2026-11-01","local":"Sala 2","organizador":"Teste"}'

{"id":4,"nome":"<script>alert(1)</script>","data":"2026-11-01","local":"Sala 2","organizador":"Teste"}
```

Na página HTML (`GET /eventos/html/lista`), o mesmo valor aparece assim no código-fonte:

```html
<strong>&lt;script&gt;alert(1)&lt;/script&gt;</strong>
```

O script **não é executado** — aparece como texto literal na tela.

**Por que input sem escape é risco de XSS?**  
Quando input do usuário é inserido em HTML sem escape, caracteres como `<` e `>` são interpretados pelo navegador como marcação real, permitindo que um atacante injete `<script>` e execute código arbitrário no navegador de quem visualiza a página. Isso pode roubar cookies de sessão, fazer requisições em nome da vítima ou desfigurar a página. O auto-escape do Jinja2 mitiga isso convertendo `<`, `>`, `"` e `&` em entidades HTML automaticamente em qualquer `{{ variavel }}` renderizada em um template `.html`, exibindo o conteúdo malicioso como texto literal em vez de executá-lo. Essa proteção não cobre valores marcados explicitamente como `| safe`.

**Herança de templates:** criado `templates/base.html` com cabeçalho e rodapé comuns; `lista.html` e `detalhe.html` usam `{% extends "base.html" %}` e preenchem apenas o bloco `{% block conteudo %}`, evitando duplicação de layout entre as páginas.

---

## Exercício 7 — Tríade CIA

| Pilar | Situação atual | Lacuna |
|---|---|---|
| **Confidencialidade** | `response_model=EventoResponse` filtra `organizador_id` e `token_auditoria` nas rotas JSON públicas | Sem autenticação/autorização: qualquer cliente acessa todos os dados. Sem HTTPS configurado no serviço. |
| **Integridade** | Pydantic valida tipos e formatos de entrada; campos obrigatórios são checados antes de persistir | Sem validações de negócio (ex: data no passado, nome duplicado). Sem logs de auditoria consultáveis. |
| **Disponibilidade** | API simples sem dependências externas que possam falhar; seeds garantem dados consistentes no startup | Sem rate limiting: sujeita a DoS por flood de requisições. Sem health check com verificação de dependências. |

---

## Exercício 8 — DFD e frameworks de referência

**Diagrama de fluxo de dados (DFD nível 0):**

![DFD do eventos-api](dfd.png)

**Componentes e trust boundaries:**

- **Entrada:** payload JSON enviado pelo cliente, originado fora da trust boundary do sistema.
- **Processamento:** validação e serialização pelos modelos Pydantic (`routes/` + `models/`), dentro do processo da API.
- **Armazenamento:** `events_db` simulado em memória (`database/db.py`), dentro da zona confiável.
- **Fluxo sensível:** `organizador_id` e `token_auditoria` são gerados e armazenados dentro da trust boundary; a única saída controlada para fora dela é filtrada pelo `response_model` (Exercício 3). Se esse controle for removido, o dado sensível atravessa a boundary sem proteção.
- **Renderização:** Jinja2 aplica auto-escape antes de retornar HTML ao cliente, formando a trust boundary de saída HTML.

**Frameworks de referência:**

| Framework | Controle de segurança concreto | Exercício |
|---|---|---|
| OWASP A03 — Injection | Auto-escape Jinja2 previne XSS via input do usuário | Exercício 6 |
| OWASP A01 — Broken Access Control | `response_model` impede exposição de campos internos | Exercício 3 |
| NIST SSDF PW.6 | Validação de input com Pydantic em todos os endpoints | Exercícios 3 e 4 |
| NIST SSDF PS.1 | Isolamento de dependências com `venv` + `requirements.txt` | Exercício 1 |
| MITRE ATT&CK T1190 | Separação de modelos interno/público mitiga enumeração | Exercício 3 |
| MITRE CWE-79 | Auto-escape de templates mitiga Cross-Site Scripting | Exercício 6 |

---

*eventos-api v0.1.0 — Guilherme Reis*
