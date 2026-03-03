from bs4 import BeautifulSoup

arquivo_html = "pagina_original.html"
lista_registros = []

try:
    with open(arquivo_html, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    tabela = soup.find("table")

    if tabela is None:
        raise ValueError("Nenhuma tabela encontrada!")

    linhas = tabela.find_all("tr")
    cabecalhos = [th.get_text(strip=True) for th in linhas[0].find_all(["th", "td"])]

    for linha in linhas[1:]:
        valores = [td.get_text(strip=True) for td in linha.find_all("td")]
        if valores:
            lista_registros.append(dict(zip(cabecalhos, valores)))

    print("Primeiros 5 registros:")
    print(lista_registros[:5])

except Exception as e:
    print("Erro ao processar tabela:", e)
