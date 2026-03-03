def executar_exercicio03():

    km_por_dia = 23
    ano_2_digitos = 25
    gasto_diario = 300 + ano_2_digitos

    print("\nOperações Aritméticas Logísticas:")
    print("Total em uma semana:", km_por_dia * 7, "km")
    print("Diferença entre 100 e gasto diario:", 100 - gasto_diario, "reais")
    print("Quantos dias R$500 cobrem:", 500 // gasto_diario)
    print("Porcentagem do gasto diário em relação a 100:", gasto_diario % 100, "%")
    print("Média diária de custo por km:", round(gasto_diario / km_por_dia, 2), "R$/km")
