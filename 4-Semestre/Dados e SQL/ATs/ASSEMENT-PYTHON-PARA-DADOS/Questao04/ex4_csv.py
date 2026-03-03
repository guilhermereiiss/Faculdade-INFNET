import csv

dicionario_indexado = {
    "PUBG Mobile": {"Jogo": "PUBG Mobile", "Jogadores": "1.1B", "Lancamento": "2018"},
    "Candy Crush Saga": {"Jogo": "Candy Crush Saga", "Jogadores": "500M", "Lancamento": "2012"},
    "Garena Free Fire": {"Jogo": "Garena Free Fire", "Jogadores": "1B", "Lancamento": "2017"}
}

try:
    chaves_colunas = list(next(iter(dicionario_indexado.values())).keys())

    with open("dados_scraping.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=chaves_colunas)
        escritor.writeheader()

        for item in dicionario_indexado.values():
            escritor.writerow(item)

    print("Arquivo 'dados_scraping.csv' salvo com sucesso!")

except Exception as e:
    print("Erro ao salvar CSV:", e)
