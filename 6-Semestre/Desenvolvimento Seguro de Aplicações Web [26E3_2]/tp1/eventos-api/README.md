# eventos-api

API REST para gerenciamento de inscrições em eventos, construída com FastAPI.

## Estrutura de módulos

```
eventos-api/
├── main.py              # Ponto de entrada da aplicação; registra routers via include_router
├── requirements.txt     # Dependências do projeto (gerado com pip freeze)
├── routes/
│   └── eventos.py       # Rotas do recurso "eventos" (GET, POST, DELETE + HTML)
├── models/
│   └── evento.py        # Modelos Pydantic: EventoCreate, EventoInterno, EventoResponse
├── database/
│   └── db.py            # Camada de acesso a dados (banco em memória); funções CRUD
└── templates/
    ├── base.html         # Template base com cabeçalho e rodapé (herança Jinja2)
    └── eventos/
        ├── lista.html    # Página HTML de listagem de eventos
        └── detalhe.html  # Página HTML de detalhe de um evento
```

### Responsabilidade de cada módulo

| Módulo | Responsabilidade |
|---|---|
| `main.py` | Inicializa o app, registra routers e hooks de startup. Não contém rotas de domínio. |
| `routes/` | Define as rotas HTTP de cada recurso. Um arquivo por domínio (ex: `eventos.py`). |
| `models/` | Define os contratos de entrada e saída da API com Pydantic. Controla o que é exposto. |
| `database/` | Encapsula o acesso e manipulação dos dados (hoje em memória; futuramente SQL/NoSQL). |
| `templates/` | Templates Jinja2 para renderização HTML server-side. Base com herança por página. |

## Como rodar

```bash
# 1. Criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Subir o servidor com hot-reload
uvicorn main:app --reload
```

## Endpoints principais

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Health check |
| GET | `/eventos/` | Lista eventos (JSON) |
| POST | `/eventos/` | Cria evento (JSON) |
| GET | `/eventos/{id}` | Obtém evento por ID (JSON) |
| DELETE | `/eventos/{id}` | Remove evento |
| GET | `/eventos/html/lista` | Lista eventos (HTML) |
| GET | `/eventos/html/{id}` | Detalhe do evento (HTML) |
| POST | `/eventos/inseguro/criar` | Demo sem response_model (Exercício 3) |

Documentação interativa disponível em `/docs` (Swagger UI).
