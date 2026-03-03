import urllib.request

url = "https://en.wikipedia.org/wiki/List_of_most-played_mobile_games_by_player_count"
arquivo_saida = "pagina_original.html"

try:
    # Criar cabeçalho User-Agent
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    resposta = urllib.request.urlopen(req)
    conteudo = resposta.read()

    with open(arquivo_saida, "wb") as f:
        f.write(conteudo)

    print("Página salva como pagina_original.html")

except Exception as e:
    print("Erro ao baixar página:", e)
