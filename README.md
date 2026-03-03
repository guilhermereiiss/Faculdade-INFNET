

```markdown
# Portfólio Acadêmico - Infnet

Repositório contendo todos os trabalhos práticos (TPs), atividades (ATs) e projetos desenvolvidos durante o curso de **Desenvolvimento Full Stack** e disciplinas correlatas na **Faculdade Infnet**.

Organizado por semestre e disciplina, com foco em:

- Desenvolvimento Web (React, Vite, CSS Modules)
- Desenvolvimento Mobile (React Native)
- Back-end e Banco de Dados (Java, C#, Python + SQL, PostgreSQL)
- Estruturas de Dados e Algoritmos
- Qualidade e Performance de Software

<br>

## 📂 Estrutura do Repositório

```text
.
├── 2-Semestre/
│   ├── MatchMovie/               # Projeto final React + API de filmes (TMDB)
│   ├── React e Mobile-First/     # ATs React + Mobile-First + React Native
│   └── TPS-React-Native/         # Trabalhos práticos React Native
│
├── 3-Semestre/
│   └── Java e C#/                # ATs e TPs em Java e C# (.NET)
│
├── 4-Semestre/
│   └── Dados e SQL/              # Python para dados, SQL, PostgreSQL, scraping
│       ├── TPS-PROJETO-DE-BLOC--DADOS/
│       ├── TPS-PB-FUNDAMENTOS-DE-DADOS/
│       └── ASSEMENT-PYTHON-PARA-DADOS/
│
├── 5-Semestre/
│   └── Linux - Velocidade e Qualidade/
│       └── TPS Velocidade e Qualidade com Estruturas de Dados e Algoritmos/
│           ├── tp1/              # Busca, ordenação, complexidade
│           └── tp2/              # Hash tables, pilhas, filas, sorts
│
├── .gitignore
├── README.md
└── repos-a-apagar.txt            # Lista de pastas antigas / experimentais
```

<br>

## 🛠️ Tecnologias e Linguagens Utilizadas

| Categoria               | Tecnologias Principais                              |
|-------------------------|------------------------------------------------------|
| Front-end               | React, React Native, Vite, CSS Modules, SCSS        |
| Mobile                  | React Native, Expo                                   |
| Back-end / Linguagens   | Java, C# (.NET), Python                              |
| Banco de Dados          | PostgreSQL, SQLite, SQLAlchemy, Entity Framework     |
| Dados & Scraping        | Pandas, BeautifulSoup, Requests                      |
| Estruturas & Algoritmos | Python (listas, dicionários, pilhas, filas, sorts)  |
| Ferramentas             | Git, npm/yarn, pip, PostgreSQL, VS Code             |

<br>

## 🚀 Principais Projetos

| Projeto / TP                              | Semestre | Tecnologias                          | Descrição resumida                                      |
|-------------------------------------------|----------|--------------------------------------|-----------------------------------------------------------------|
| **MatchMovie**                            | 2º       | React, Vite, Context API             | App de filmes com autenticação, favoritos e detalhes (TMDB API) |
| **Loopify – Gerenciador de Playlists**    | 4º       | Python                               | Sistema console para gerenciar músicas, urgência e prazos      |
| **Mercadinho (TP3 – Banco de Dados)**     | 4º       | PostgreSQL, SQLAlchemy               | Modelo relacional + joins + operações CRUD via JSON/upsert     |
| **PyMusic Scraper (TP5)**                 | 4º       | Python, BeautifulSoup, PostgreSQL    | Web scraper de álbuns musicais da Wikipédia com persistência   |
| **Estruturas e Algoritmos (TPs 1 e 2)**   | 5º       | Python                               | Implementações de pilhas, filas, sorts e hash tables            |

<br>

## Como Navegar

1. Escolha o **semestre** de interesse  
2. Dentro dele, procure a pasta da **disciplina** ou **TP/AT**  
3. A maioria dos projetos tem um pequeno **README.md** interno com instruções de execução

Exemplos de comandos comuns:

```bash
# React / Vite (ex: MatchMovie)
cd 2-Semestre/MatchMovie/MatchMovie
npm install
npm run dev

# Python (ex: Loopify ou scraper)
cd 4-Semestre/Dados\ e\ SQL/TPS-PB-FUNDAMENTOS-DE-DADOS
python main.py

# Banco de dados (PostgreSQL)
psql -U postgres -d tp3-pb -f comandos01.sql
```

<br>

## 📝 Observações Importantes

- Alguns projetos requerem **PostgreSQL** configurado localmente (veja arquivos `.sql` e strings de conexão nos códigos).
- Muitos projetos foram desenvolvidos em **ambiente Windows** → caminhos de arquivo podem precisar de ajuste em Linux/Mac.
- Pastas listadas em `repos-a-apagar.txt` são antigas/experimentos e podem ser removidas futuramente.
- **Senhas de banco de dados** estão hardcoded apenas para fins acadêmicos — **nunca** use em produção!

<br>

## 📬 Contato

- **Nome**: Guilherme Reis  
- **LinkedIn**: [linkedin.com/in/guilherme-reis-d3v](https://www.linkedin.com/in/guilherme-reis-d3v/)  
- **E-mail**: guiprogramador06@gmail.com  

Infnet – 2024–2026

Última atualização: Março 2026
```
