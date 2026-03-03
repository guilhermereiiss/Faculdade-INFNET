# Exemplos de tipos de dados em Python
# Cada variável abaixo representa um tipo diferente de dado.
# Usamos a função type() para exibir o tipo de cada variável.

# -------------------------------
# int → Tipo inteiro
# Representa números inteiros (positivos, negativos ou zero), sem casas decimais.
num_inteiro = 13
print("O número inteiro é:", num_inteiro)
print("Tipo:", type(num_inteiro))
print()

# -------------------------------
# float → Tipo ponto flutuante
# Representa números reais, com parte decimal (casas decimais).
altura = 1.75
print("A altura é:", altura)
print("Tipo:", type(altura))
print()

# -------------------------------
# str → String
# Representa texto, ou seja, uma sequência de caracteres entre aspas.
nome = "Guilherme"
print("O nome é:", nome)
print("Tipo:", type(nome))
print()

# -------------------------------
# bool → Booleano
# Representa um valor lógico: True (verdadeiro) ou False (falso).
maior_de_idade = True
print("É maior de idade?", maior_de_idade)
print("Tipo:", type(maior_de_idade))
print()

# -------------------------------
# list → Lista
# Representa uma coleção de valores que pode ser modificada (mutável).
# Os itens são ordenados e podem ser de tipos diferentes.
frutas = ["maçã", "banana", "uva"]
print("Lista de frutas:", frutas)
print("Tipo:", type(frutas))
print()

# -------------------------------
# tuple → Tupla
# Representa uma coleção de valores que não pode ser modificada (imutável).
# Também é ordenada, como a lista.
coordenada = (4, 7)
print("Coordenada:", coordenada)
print("Tipo:", type(coordenada))
print()

# -------------------------------
# dict → Dicionário
# Armazena pares de chave e valor. Muito útil para representar objetos.
# Exemplo: nome de uma pessoa e sua idade.
pessoa = {"nome": "Maria", "idade": 30}
print("Dados da pessoa:", pessoa)
print("Tipo:", type(pessoa))
print()

# -------------------------------
# NoneType → Tipo especial que representa ausência de valor
# Usado quando uma variável ainda não recebeu um valor definido.
resposta = None
print("Resposta:", resposta)
print("Tipo:", type(resposta))
print()

# -------------------------------
# int com valor negativo
# Números negativos também fazem parte do tipo int.
temperatura = -5
print("Temperatura:", temperatura)
print("Tipo:", type(temperatura))
print()

# -------------------------------
# Outro exemplo de str (usando aspas simples)
# É possível criar strings com aspas simples ou duplas.
mensagem = 'Olá, mundo!'
print("Mensagem:", mensagem)
print("Tipo:", type(mensagem))
