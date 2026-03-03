lista_de_dicionarios = [
    {"Jogo": "PUBG Mobile", "Jogadores": "1.1B", "Lançamento": "2018"},
    {"Jogo": "Candy Crush Saga", "Jogadores": "500M", "Lançamento": "2012"},
    {"Jogo": "Garena Free Fire", "Jogadores": "1B", "Lançamento": "2017"},
    {"Jogo": "Candy Crush Saga", "Jogadores": "500M", "Lançamento": "2012"}
]

coluna_chave = "Jogo"

dicionario_indexado = {}
valores_repetidos = {}

for linha in lista_de_dicionarios:
    valor = linha[coluna_chave]
    if valor not in valores_repetidos:
        valores_repetidos[valor] = 0
    valores_repetidos[valor] += 1
    dicionario_indexado[valor] = linha

conjunto_valores = {linha[coluna_chave] for linha in lista_de_dicionarios}

total_registros = len(lista_de_dicionarios)
total_unicos = len(conjunto_valores)

duplicatas = [valor for valor, cont in valores_repetidos.items() if cont > 1]

print("Dicionário Indexado:")
print(dicionario_indexado)

print(f"\nTotal de registros: {total_registros}")
print(f"Total de valores únicos: {total_unicos}")
print(f"Duplicatas encontradas: {duplicatas}")
