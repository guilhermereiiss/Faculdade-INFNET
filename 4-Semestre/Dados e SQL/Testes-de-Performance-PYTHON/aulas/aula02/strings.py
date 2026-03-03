# Criação de string com aspas triplas (permite múltiplas linhas)
texto = """Esse é um texto
em várias linhas"""
print(texto)

# Remove espaços em branco no início e no fim
frase = "   Python é legal!   "
print(frase.strip())

# Verifica se a string começa com determinado texto
mensagem = "Aprender Python é divertido"
print(mensagem.startswith("Aprender"))  # True

# Verifica se a string termina com determinado texto
print(mensagem.endswith("divertido"))  # True

# Substitui partes da string
frase = "O céu é azul"
print(frase.replace("azul", "vermelho"))

# Divide a string em uma lista de palavras
frase = "Python é muito bom"
palavras = frase.split()
print(palavras)  # ['Python', 'é', 'muito', 'bom']

# Junta os itens de uma lista em uma única string
print(" ".join(palavras))  # Python é muito bom

# Conta quantas vezes uma substring aparece
print(frase.count("o"))  # Conta quantas vezes 'o' aparece

# Encontra o índice de uma substring
print(frase.find("muito"))  # Retorna o índice onde começa "muito"

# Verifica se todos os caracteres são numéricos
numero = "12345"
print(numero.isdigit())  # True

# Verifica se todos os caracteres são letras
nome = "Python"
print(nome.isalpha())  # True

# Verifica se todos os caracteres são minúsculos
print(nome.islower())  # False

# Verifica se todos os caracteres são maiúsculos
print(nome.isupper())  # False
