
## LOGIN: admin / SENHA: 12345

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/e/ee/.NET_Core_Logo.svg" width="120" alt="Logo .NET" />
</p>

# AgenciaViagem

## Sobre o Projeto

O projeto **AgenciaViagem** é uma aplicação web desenvolvida em **ASP.NET Core (Razor Pages)** com uso de **Entity Framework Core** e banco de dados **SQLite**.

O sistema tem como objetivo gerenciar os principais dados de uma agência de turismo, permitindo o cadastro, consulta e administração de:

* Clientes
* Pacotes Turísticos
* Reservas
* Cidades Destinos
* Países Destinos

A aplicação também inclui autenticação de usuários, controle de acesso, validações de formulário e uma interface com layout responsivo utilizando Bootstrap.

## Estrutura de Pastas do Projeto

```
AgenciaViagem/
├── Data/
│   └── AgenciaViagemContext.cs
├── Migrations/
│   ├── InitialCreate.cs
│   ├── InitialCreate.Designer.cs
│   └── AgenciaViagemContextModelSnapshot.cs
├── Models/
│   ├── CidadeDestino.cs
│   ├── Cliente.cs
│   ├── PacoteTuristico.cs
│   ├── PaisDestino.cs
│   └── Reserva.cs
├── Pages/
│   ├── Clientes/
│   ├── Pacotes/
│   ├── Reservas/
│   ├── Shared/
│   ├── Index.cshtml
│   ├── Login.cshtml
│   ├── Logout.cshtml
│   └── Error.cshtml
├── wwwroot/
│   ├── css/
│   ├── js/
│   └── lib/
├── Program.cs
├── appsettings.json
├── appsettings.Development.json
└── AgenciaViagem.csproj
```

## Tecnologias Utilizadas

* ASP.NET Core 9 (Razor Pages)
* Entity Framework Core
* SQLite
* Bootstrap
* jQuery e jQuery Validation

## Requisitos para Execução

* SDK .NET 9.0 ou superior
* Editor de código (Visual Studio 2022 ou VS Code)

## Como Executar o Projeto

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/AgenciaViagem.git
```

2. Acesse a pasta do projeto:

```
cd AgenciaViagem
```

3. Restaure os pacotes NuGet:

```
dotnet restore
```

4. Crie o banco de dados a partir da migration:

```
dotnet ef database update
```

5. Execute a aplicação:

```
dotnet run
```

6. Acesse no navegador:

```
https://localhost:5001
```

## Funcionalidades Implementadas

* Cadastro, consulta e listagem de Clientes
* Cadastro e listagem de Pacotes Turísticos
* Gestão de Reservas com cálculo de valor total
* Relacionamento entre Pacotes, Cidades e Países
* Validações de dados nos formulários
* Controle de login, logout e permissões de acesso
* Layout responsivo com Bootstrap

## Estrutura de Banco de Dados

* Tabela de Clientes
* Tabela de Pacotes Turísticos
* Tabela de Reservas
* Tabela de Cidades Destinos
* Tabela de Países Destinos

## Migration Inicial

* `20250620035431_InitialCreate`

## Autor

Guilherme Reis


