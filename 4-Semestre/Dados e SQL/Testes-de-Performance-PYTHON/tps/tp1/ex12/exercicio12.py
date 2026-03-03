def executar_exercicio12():

    desconto_txt = "23"
    desconto_num = float(desconto_txt) / 3.14
    valor_produto = 599.99
    valor_final = valor_produto - (valor_produto * desconto_num / 100)

    print("\nCálculo de Desconto:")
    print("Percentual de desconto:", round(desconto_num, 2), "%")
    print("Valor final do produto: R$", round(valor_final, 2))
