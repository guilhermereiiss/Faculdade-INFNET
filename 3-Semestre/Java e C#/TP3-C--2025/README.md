

---

# Sistema de Venda de Ingressos e Matrículas em C#

![C# Logo](https://i.ibb.co/JWDzb9n5/Blue-and-Black-Modern-Coding-School-Presentation.png)

## Descrição

Este repositório contém um conjunto de exercícios desenvolvidos em **C#** que exploram conceitos fundamentais da **Programação Orientada a Objetos (POO)**, como classes, objetos, campos (atributos), métodos e construtores. Além disso, o sistema desenvolvido simula uma venda de ingressos para um show e a gestão de matrículas em uma faculdade, permitindo a manipulação e exibição de informações através de métodos e propriedades.

Os exercícios são seguidos de exemplos práticos que demonstram a utilização dos conceitos aprendidos.

## Exercícios

1. **Conceitos de Classe, Objeto, Campos e Métodos (C#)**  
   Explicação dos conceitos de classe, objeto, atributos e métodos, com exemplos práticos.

2. **Criando a Classe "Ingresso"**  
   Criação da classe `Ingresso` com atributos básicos como nome do show, preço e quantidade disponível.

3. **Métodos Básicos da Classe "Ingresso"**  
   Implementação de métodos para atualizar o preço, a quantidade disponível e exibir as informações do ingresso.

4. **Testando a Classe "Ingresso"**  
   Teste da classe `Ingresso` com instância de objetos, chamada de métodos e exibição dos resultados.

5. **Métodos de Propriedade (Getters e Setters)**  
   Criação de métodos para acessar e alterar os valores dos atributos da classe `Ingresso`.

6. **Adicionando Construtores à Classe "Ingresso"**  
   Criação de construtores para inicializar a classe `Ingresso` de forma mais eficiente.

7. **Modelando uma Matrícula**  
   Criação de uma classe `Matricula` para representar uma matrícula de aluno, com atributos como nome do aluno, curso, número de matrícula, situação e data de início.

8. **Métodos na Classe "Matricula"**  
   Adição de métodos para alterar a situação da matrícula (trancar e reativar) e exibir informações.

9. **Testando a Classe de Matrícula**  
   Teste da classe `Matricula` com a atribuição de valores aos atributos e a chamada dos métodos para manipulação da matrícula.

10. **Definindo Classes de Formas Geométricas (Círculo e Esfera)**  
    Criação de classes para representar o círculo e a esfera, com o atributo `Raio`.

11. **Criando Métodos de Cálculo (Área e Volume)**  
    Adição de métodos para calcular a área do círculo e o volume da esfera.

12. **Testando as Classes de Figuras Geométricas**  
    Teste das classes de círculo e esfera, com a exibição dos resultados dos cálculos.

## Estrutura do Código

### Classes Principais

- **Ingresso**: Representa um ingresso para o show, com atributos para nome, preço e quantidade disponível, além de métodos para alterar essas propriedades e exibir informações.
- **Matricula**: Representa uma matrícula de aluno, com atributos como nome, curso, número da matrícula, situação e data de início. Métodos para trancar, reativar e exibir informações também estão presentes.
- **Figuras Geométricas**: Contém as classes `Circulo` e `Esfera`, cada uma com um atributo `Raio` e métodos para calcular área ou volume.

### Exemplos de Uso

#### Classe `Ingresso`

```csharp
Ingresso ingresso = new Ingresso("Show Rock", 100.0, 200);
ingresso.AlterarPreco(120.0);
ingresso.AlterarQuantidade(150);
ingresso.ExibirInformacoes();
```

#### Classe `Matricula`

```csharp
Matricula matricula = new Matricula("João Silva", "Engenharia", 12345, "Ativa", "01/02/2024");
matricula.Trancar();
matricula.ExibirInformacoes();
matricula.Reativar();
matricula.ExibirInformacoes();
```

#### Classe `Circulo` e `Esfera`

```csharp
Circulo circulo = new Circulo(3.0);
Console.WriteLine("Área do Círculo: " + circulo.CalcularArea());

Esfera esfera = new Esfera(5.0);
Console.WriteLine("Volume da Esfera: " + esfera.CalcularVolume());
```

## Tecnologias Utilizadas

- **C#**: Linguagem de programação orientada a objetos.
- **.NET**: Framework utilizado para desenvolvimento em C#.

## Como Executar

Para rodar os exemplos no seu ambiente de desenvolvimento, siga as instruções abaixo:

1. **Clonar o repositório**:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. **Abrir o projeto no Visual Studio**:

- Abra o arquivo `.sln` no Visual Studio ou qualquer outro editor C# que preferir.

3. **Executar o projeto**:

- Compile e execute o código usando o Visual Studio.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
