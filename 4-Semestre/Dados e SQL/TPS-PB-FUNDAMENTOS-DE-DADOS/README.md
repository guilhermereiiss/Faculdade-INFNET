# Loopify - Gerenciador de Playlist

Um sistema simples e intuitivo para gerenciar suas músicas favoritas desenvolvido em Python.

## Sobre o Projeto

O Loopify é um gerenciador de playlist que permite adicionar, listar, marcar como tocadas e remover músicas de forma prática através de um menu interativo no terminal. Ideal para quem quer organizar suas músicas de forma simples e eficiente.

## Funcionalidades

-  **Adicionar música**: Inclua novas músicas com título, artista, prazo final e nível de urgência
-  **Listar músicas**: Visualize todas as músicas da playlist com detalhes completos
-  **Marcar como tocada**: Controle quais músicas já foram ouvidas
-  **Remover música**: Exclua músicas que não deseja mais na playlist
-  **Sistema de urgência**: Marque músicas como urgentes para priorizar
-  **Controle de prazos**: Defina prazos limite para ouvir suas músicas

## Como Usar

### Pré-requisitos

- Python 3.6 ou superior

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/loopify.git
```

2. Navegue até o diretório do projeto:
```bash
cd loopify
```

3. Execute o programa:
```bash
python main.py
```

### Navegação no Menu

Ao executar o programa, você verá o menu principal com as seguintes opções:

```
=== Loopify - Gerenciador de Playlist ===
1 - Adicionar música
2 - Listar músicas
3 - Marcar música como tocada
4 - Remover música
5 - Sair
```

## Estrutura do Projeto

```
loopify/
│
├── data/
│   └── dados.py          # Armazenamento da playlist e contador de IDs
├── funcoes.py            # Funções principais do sistema
├── main.py               # Menu principal e interface do usuário
└── README.md            # Documentação do projeto
```

## Funcionalidades Detalhadas

### Adicionar Música
- Informe título e artista
- Defina um prazo final (opcional)
- Marque como urgente se necessário
- A música recebe automaticamente um ID único e data de inclusão

### Listar Músicas
Exibe todas as músicas com:
- ID único
- Título e artista
- Status (Pendente/Tocada)
- Nível de urgência
- Prazo final (se definido)

### Marcar como Tocada
- Selecione uma música pelo ID
- O status é alterado de "Pendente" para "Tocada"

### Remover Música
- Selecione uma música pelo ID
- A música é permanentemente removida da playlist

## Tecnologias Utilizadas

- **Python 3**: Linguagem principal
- **datetime**: Para controle de datas
- **Estruturas de dados**: Listas e dicionários para armazenamento
