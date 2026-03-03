# ========================
# 1) Loop FOR
# ========================
# ========================
# EXEMPLO 1: Contar de 1 até 5
# ========================
print("Exemplo 1 - Contando de 1 até 5:")
for numero in range(1, 6):  # Gera: 1, 2, 3, 4, 5
    print(numero)

for numero in range(6):  # Gera: 0,1, 2, 3, 4, 5
    print(numero)

# ========================
# EXEMPLO 2: Contar de 0 até 10 pulando de 2 em 2
# ========================
print("\nExemplo 2 - Contando de 0 até 10, de 2 em 2:")
for numero in range(0, 11, 2):  # Gera: 0, 2, 4, 6, 8, 10
    print(numero)


# ========================
# EXEMPLO 3: Contar de trás para frente
# ========================
print("\nExemplo 3 - Contagem regressiva:")
for numero in range(10, 0, -1):  # Começa no 10, vai até 1, de -1 em -1
    print(numero)


# ========================
# EXEMPLO 4: Percorrer letras de uma palavra
# ========================
print("\nExemplo 4 - Letras de uma palavra:")
palavra = "Python"
for letra in palavra:  # Cada volta, 'letra' recebe um caractere da palavra
    print(letra)


# ========================
# EXEMPLO 5: Somar números de uma lista
# ========================
print("\nExemplo 5 - Somando elementos de uma lista:")
numeros = [5, 8, 12, 3]
soma = 0
for n in numeros:
    soma += n  # soma = soma + n
print(f"Soma total: {soma}")


# ========================
# EXEMPLO 6: Usando for com if
# ========================
print("\nExemplo 6 - Mostrar apenas números pares de 1 a 10:")
for numero in range(1, 11):
    if numero % 2 == 0:  # Verifica se é par
        print(numero)



# ========================
# 2) Loop WHILE
# ========================
print("\nUsando WHILE:")

# O 'while' repete enquanto a condição for verdadeira.
contador = 1  # Começamos o contador com 1
while contador <= 5:  # Enquanto o contador for menor ou igual a 5
    print(f"Número: {contador}")  # Mostra o valor atual
    contador += 1  # Incrementa o contador (contador = contador + 1)
    # Quando 'contador' ficar maior que 5, o loop para


# ========================
# 3) Simulando DO WHILE
# ========================
print("\nSimulando DO WHILE:")

# O 'do while' não existe no Python, mas podemos simular.
# A diferença é que ele executa pelo menos UMA vez antes de verificar a condição.
contador = 1
while True:  # Loop infinito, vamos parar manualmente
    print(f"Número: {contador}")  # Executa pelo menos uma vez
    contador += 1  # Incrementa o contador
    if contador > 5:  # Verifica a condição de parada no FINAL do loop
        break  # Sai do loop
