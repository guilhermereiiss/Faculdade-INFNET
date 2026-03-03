import json

dicionario_indexado = {
    "PUBG Mobile": {"Jogo": "PUBG Mobile", "Jogadores": "1.1B", "Lancamento": "2018"},
    "Candy Crush Saga": {"Jogo": "Candy Crush Saga", "Jogadores": "500M", "Lancamento": "2012"},
    "Garena Free Fire": {"Jogo": "Garena Free Fire", "Jogadores": "1B", "Lancamento": "2017"}
}


try:
    with open("dados_scraping.json", "w", encoding="utf-8") as arquivo_json:
        json.dump(dicionario_indexado, arquivo_json, indent=4, ensure_ascii=False)
    print("Arquivo 'dados_scraping.json' salvo com sucesso!")
except Exception as e:
    print("Erro ao salvar JSON:", e)

try:
    with open("dados_scraping.json", "r", encoding="utf-8") as arquivo_json:
        dados_lidos = json.load(arquivo_json)
        print("\nConteúdo do arquivo JSON:")
        print(dados_lidos)
except Exception as e:
    print("Erro ao ler JSON:", e)
