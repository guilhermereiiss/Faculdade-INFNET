def extrair_versao(nome_arquivo):
    indice_ponto = nome_arquivo.find(".")
    
    if indice_ponto == -1:
        return None  

    antes_extensao = nome_arquivo[:indice_ponto]

    partes = antes_extensao.split("_")
    return partes[-1] if partes else None


def main05():
    nome_arquivo = "relat_2024_final_v2.csv"

    comeca_com_relat = nome_arquivo.startswith("relat_")

    contem_final = nome_arquivo.find("final") != -1

    versao = extrair_versao(nome_arquivo)

    print("Começa com 'relat_'?", comeca_com_relat)
    print("Contém 'final'?", contem_final)
    print("Versão do arquivo:", versao)
