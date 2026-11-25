# Portfólio Acadêmico - Infnet

Repositório contendo todos os trabalhos práticos (TPs), atividades (ATs) e projetos desenvolvidos durante a graduação na **Faculdade Infnet**.

Organizado por semestre e disciplina, com foco em:

- Desenvolvimento Web (React, Vite, CSS Modules)
- Desenvolvimento Mobile (React Native)
- Back-end e Banco de Dados (Java, C#, Python + SQL, PostgreSQL, SQLite)
- Estruturas de Dados, Algoritmos e Programação Distribuída com Linux e Python
- Estatística Aplicada e Análise Exploratória de Dados
- Segurança de Aplicações Web, Pentest e Análise de Vulnerabilidades
- Machine Learning, Modelagem Preditiva e Construção de Agentes de IA

<br>

## 📂 Estrutura do Repositório

```text
.
├── 2-Semestre/
│   ├── MatchMovie/                                           # Projeto final React + API de filmes (TMDB)
│   └── React e Mobile-First/                                 # ATs e TPs de React, Mobile-First e React Native
│
├── 3-Semestre/
│   └── Java e C#/                                            # ATs e TPs em Java e C# (.NET)
│
├── 4-Semestre/
│   └── Dados e SQL/                                          # Python para dados, SQL, PostgreSQL e scraping
│
├── 5-Semestre/
│   ├── Estruturas de Dados e Algoritmos Avançados [26E2_3]/  # TP1–TP3 e AT (grafos, algoritmos avançados)
│   ├── Linux -  Velocidade e Qualidade/                      # TPs de Estruturas de Dados e performance
│   ├── Linux - Projeto de Bloco/                             # Projeto de Bloco com Linux e Python
│   ├── Programação Distribuída com Redes usando Linux e Python [26E2_4]/  # Sockets TCP/UDP, HTTP, TLS, IPv6
│   └── Sistemas Operacionais com Linux e Python/             # AT com Docker e simulação Monte Carlo
│
├── 6-Semestre/
│   ├── Análise de Vulnerabilidades e Pentest Web/            # Laboratório OWASP crAPI (Docker Compose)
│   ├── Desenvolvimento Seguro de Aplicações Web [26E3_2]/    # TP1–TP3 (eventos-api) e AT (clínica segura + OWASP ZAP)
│   ├── Estatística Aplicada e Análise Exploratória de Dados [26E3_1]/  # TP1–TP3 (suporte/triagem) e AT (dataset Olist)
│   ├── Modelagem Preditiva e Construção de Agentes de IA/    # TP1–TP2 (ML churn/LTV NeoStream) e TP3 (Agentes IA SDK)
│   │   ├── tp1/                                              # Pipeline sklearn, ColumnTransformer, GridSearchCV, data leakage
│   │   ├── tp2/                                              # Matriz de confusão, ROC-AUC, sigmoide/softmax, SVM linear e RBF
│   │   └── tp3/                                              # Agentes de IA (openai-agents SDK, Pydantic, execução assíncrona)
│   └── Projeto de Bloco - Análise e Segurança/               # Projeto de Bloco do 6º semestre
│
└── README.md
```

<br>

## 🛠️ Tecnologias e Linguagens Utilizadas

| Categoria | Tecnologias Principais |
|---|---|
| Front-end | React, Vite, CSS Modules, SCSS |
| Mobile | React Native, Expo |
| Back-end / Linguagens | Python, Java, C# (.NET) |
| Banco de Dados | PostgreSQL, SQLite, SQLAlchemy, Entity Framework |
| Dados & Estatística | Pandas, NumPy, Matplotlib, Jupyter Notebook, BeautifulSoup |
| Machine Learning & IA | scikit-learn, joblib, OpenAI Agents SDK (`openai-agents`), Pydantic, `asyncio` |
| Redes, SO & Segurança | Linux, Docker / Docker Compose, Sockets TCP/UDP, TLS, OWASP ZAP, OWASP crAPI |
| Ferramentas | Git, GitHub, npm/yarn, pip/venv, VS Code |

<br>

## 🚀 Principais Projetos

| Projeto / Entrega | Semestre | Tecnologias | Descrição resumida |
|---|---|---|---|
| **MatchMovie** | 2º | React, Vite, Context API | App de filmes com autenticação, favoritos e detalhes (TMDB API) |
| **Loopify – Gerenciador de Playlists** | 4º | Python | Sistema console para gerenciar músicas, urgência e prazos |
| **Mercadinho (TP3 – Banco de Dados)** | 4º | PostgreSQL, SQLAlchemy | Modelo relacional, joins e operações CRUD via JSON/upsert |
| **PyMusic Scraper (TP5)** | 4º | Python, BeautifulSoup, PostgreSQL | Web scraper de álbuns musicais da Wikipédia com persistência |
| **Estruturas de Dados & Redes (TPs e ATs)** | 5º | Python, Linux, Docker, Sockets, TLS | Grafos, algoritmos avançados, servidores TCP/UDP/HTTP concorrentes e Docker |
| **EDA & Estatística Aplicada (TP1–TP3 e AT)** | 6º | Python, Pandas, Jupyter | Análise exploratória de tickets de suporte e do e-commerce brasileiro (Olist) |
| **Desenvolvimento Seguro (eventos-api e AT)** | 6º | Python, SQLite, Pytest, OWASP ZAP | API segura com autenticação, middlewares defensivos e análise DAST com ZAP |
| **Churn & LTV NeoStream (TP1 e TP2)** | 6º | Python, scikit-learn, joblib, Matplotlib | Pipeline sem data leakage, tuning com `GridSearchCV`, ROC-AUC, sigmoide/softmax e SVM (linear e RBF) |
| **Agente de Retenção NeoStream (TP3)** | 6º | Python, `openai-agents`, Pydantic, `asyncio` | Agente de IA com saída estruturada validada e execução assíncrona concorrente para análise de churn |

<br>

## 🧭 Como Navegar

1. Escolha o **semestre** de interesse.
2. Dentro dele, acesse a pasta da **disciplina** e do **TP** ou **AT**.
3. Projetos mais recentes trazem `requirements.txt`, `.env.example` ou documentação `.md` interna com instruções de execução.

Exemplos de comandos comuns:

```bash
# React / Vite (ex.: MatchMovie)
cd 2-Semestre/MatchMovie/MatchMovie
npm install
npm run dev

# Agentes de IA - TP3 (Modelagem Preditiva e Construção de Agentes de IA)
cd "6-Semestre/Modelagem Preditiva e Construção de Agentes de IA/tp3"
python -m venv .venv
# Windows: .\.venv\Scripts\Activate.ps1 | Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # preencha com sua chave de API
python verificar_ambiente.py
python agente_churn_final.py

# Laboratório OWASP crAPI (Análise de Vulnerabilidades e Pentest Web)
cd "6-Semestre/Análise de Vulnerabilidades e Pentest Web/tp1/crapi"
docker compose up -d
```

<br>

## 📝 Observações Importantes

- Alguns projetos do 4º semestre requerem **PostgreSQL** configurado localmente (veja os arquivos `.sql` e strings de conexão nos códigos).
- Projetos de Agentes de IA utilizam variáveis de ambiente via `.env` (ignorado pelo Git) com modelo documentado em `.env.example` — **nunca** versione chaves reais de API.
- Projetos mais antigos contêm credenciais fictícias/didáticas hardcoded apenas para fins acadêmicos — nunca utilize em produção.
- A maior parte dos projetos foi desenvolvida em ambiente **Windows** (alguns caminhos de arquivo podem exigir ajuste em Linux/macOS).

<br>

## 📬 Contato

- **Nome**: Guilherme Reis
- **LinkedIn**: [linkedin.com/in/guilherme-reis-d3v](https://www.linkedin.com/in/guilherme-reis-d3v/)
- **E-mail**: guiprogramador06@gmail.com

Infnet – 2024–2026

Última atualização: Novembro 2026
