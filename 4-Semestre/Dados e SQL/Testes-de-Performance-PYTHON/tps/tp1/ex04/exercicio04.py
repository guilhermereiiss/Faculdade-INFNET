def executar_exercicio04():

    ano_2_digitos = 25
    tempo_minutos = 150 + ano_2_digitos  
    tempo_horas = 2.25

    horas_convertidas = round(tempo_minutos / 60, 2)
    minutos_convertidos = tempo_horas * 60

    print("\nConversão de Tempo:")
    print(f"{tempo_minutos} minutos é igual a {horas_convertidas} horas")
    print(f"{tempo_horas} horas é igual a {minutos_convertidos} minutos")
