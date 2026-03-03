def extrair_codigos(mensagem):

    resultados = []
    i = 0
    while i < len(mensagem):
        if mensagem[i] == "@":
            # Encontrar o próximo #
            fim = i + 1
            while fim < len(mensagem) and mensagem[fim] != "#":
                fim += 1
            if fim < len(mensagem):
                # Extrair conteúdo entre @ e #
                trecho = mensagem[i+1:fim]
                # Remover caracteres inválidos
                codigo_limpo = ""
                for char in trecho:
                    if char.isalnum():
                        codigo_limpo += char
                if codigo_limpo:
                    resultados.append(codigo_limpo)
                i = fim  # pular para depois do #
        i += 1
    return resultados


def main12():
    mensagem = "Sensor detectado: @A1B2C3# fora de faixa. Erro: @ 9X # ignorado. Validação: @99Z#"
    
    print("Mensagem original:")
    print(mensagem)
    
    codigos = extrair_codigos(mensagem)
    
    print("\nCódigos extraídos e limpos:")
    print(codigos)


