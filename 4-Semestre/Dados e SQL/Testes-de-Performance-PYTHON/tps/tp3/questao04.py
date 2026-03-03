def extrair_termo(url):
    """
    Extrai o valor do parâmetro 'termo' de uma URL.
    Não usa bibliotecas externas, apenas métodos padrão de string.
    """
    if "?" in url:
        parametros = url.split("?", 1)[1]  
    else:
        return None 

    for par in parametros.split("&"):
        if par.startswith("termo="):
            return par.split("=", 1)[1]

    return None 


def main04():
    url = "https://sistema.exemplo.com/busca?termo=velho"

    url_nova = url.replace("velho", "novo")

    termo_extraido = extrair_termo(url_nova)

    print("URL original:", url)
    print("URL nova:", url_nova)
    print("Termo extraído:", termo_extraido)
