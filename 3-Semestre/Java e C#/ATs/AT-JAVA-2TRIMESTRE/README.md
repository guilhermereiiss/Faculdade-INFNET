# To do API

Uma API REST simples para gerenciamento de tarefas desenvolvida em Java usando Javalin framework.

![Java](https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg)

## Tecnologias Utilizadas

- **Java** - Linguagem de programação principal
- **Javalin** - Framework web minimalista para Java
- **Jackson** - Biblioteca para serialização/deserialização JSON
- **Gradle** - Ferramenta de build e gerenciamento de dependências
- **JUnit 5** - Framework de testes unitários

## Funcionalidades

- Criar tarefas individuais ou em lote
- Listar todas as tarefas
- Buscar tarefa por ID
- Verificar status da API
- Endpoint de saudação personalizada
- Echo endpoint para testes

## Estrutura do Projeto

```
src/
├── main/java/org/example/
│   ├── api/
│   │   ├── ApiClient.java          # Cliente HTTP básico para testes
│   │   └── TaskApi.java            # Definição das rotas da API
│   ├── client/                     # Clientes HTTP utilitários
│   │   ├── HttpClientUtil.java     # Utilitário para requisições HTTP
│   │   ├── StatusClient.java       # Cliente para endpoint de status
│   │   ├── TaskByIdClient.java     # Cliente para buscar tarefa por ID
│   │   ├── TaskClient.java         # Cliente para criar tarefas
│   │   └── TaskListClient.java     # Cliente para listar tarefas
│   ├── config/
│   │   ├── ApiResponse.java        # Classe para respostas da API
│   │   └── StatusInfo.java         # Classe para informações de status
│   ├── dto/
│   │   └── TaskDTO.java            # Data Transfer Object para tarefas
│   ├── storage/
│   │   └── TaskStorage.java        # Armazenamento em memória das tarefas
│   ├── Application.java            # Classe principal da aplicação
│   └── Main.java                   # Classe main alternativa
└── test/java/org/example/api/
    └── TaskApiTest.java            # Testes unitários da API
```

## Endpoints da API

### Status
- `GET /status` - Retorna o status da API com timestamp

### Saudação
- `GET /hello` - Retorna "Hello, Javalin!"
- `GET /saudacao/{nome}` - Retorna saudação personalizada

### Echo
- `POST /echo` - Retorna a mensagem enviada no corpo da requisição

### Tarefas
- `POST /tasks` - Cria uma nova tarefa ou lista de tarefas
- `GET /tasks` - Lista todas as tarefas
- `GET /tasks/{id}` - Busca tarefa por ID

## Modelo de Tarefa

```json
{
  "id": 1,
  "titulo": "Título da tarefa",
  "descricao": "Descrição da tarefa",
  "concluida": false,
  "dataCriacao": "2025-06-17T15:30:45"
}
```

## Como Executar

### Pré-requisitos
- Java 21 ou superior
- Gradle (ou usar o wrapper incluído)

### Passos para execução

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd AT-JAVA-2TRI-OFC
   ```

2. **Execute a aplicação**
   ```bash
   # Usando Gradle wrapper (recomendado)
   ./gradlew run
   
   # Ou compile e execute manualmente
   ./gradlew build
   java -cp build/libs/* org.example.Application
   ```

3. **A API estará disponível em**: `http://localhost:7000`

### Executar os testes

```bash
# Executar todos os testes
./gradlew test

# Ver relatório de testes
./gradlew test --info
```

## Testando a API

### Usando curl

**Criar uma tarefa:**
```bash
curl -X POST http://localhost:7000/tasks \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Minha Tarefa", "descricao": "Descrição da tarefa", "concluida": false}'
```

**Listar tarefas:**
```bash
curl http://localhost:7000/tasks
```

**Buscar tarefa por ID:**
```bash
curl http://localhost:7000/tasks/1
```

**Verificar status:**
```bash
curl http://localhost:7000/status
```

### Usando os clientes incluídos

O projeto inclui classes cliente para testar os endpoints:

```bash
# Executar o cliente básico
java -cp build/libs/* org.example.api.ApiClient
```

## Exemplo de Uso

1. Inicie a aplicação
2. Crie algumas tarefas via POST
3. Liste todas as tarefas via GET
4. Busque uma tarefa específica por ID
5. Verifique o status da API

## Armazenamento

As tarefas são armazenadas **em memória** durante a execução da aplicação. Quando a aplicação é reiniciada, todos os dados são perdidos. Cada tarefa recebe automaticamente:
- ID único incremental
- Data/hora de criação no formato ISO

## Licença

Este projeto é desenvolvido para fins educacionais.

---

**Desenvolvido usando Java e Javalin**
