print("Calculadora do Ryuu")

while True:  
    valor1 = float(input("\nDigite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    print("\nAgora escolha a operação")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Encerrando a calculadora")
        break

    while opcao < 1 or opcao > 4:
        print("Opção invalida! Escolha novamente.")
        opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        resultado = valor1 + valor2
        print(f"Resultado da soma: {resultado}")
    elif opcao == 2:
        resultado = valor1 - valor2
        print(f"Resultado da subtração: {resultado}")
    elif opcao == 3:
        resultado = valor1 * valor2
        print(f"Resultado da multiplicação: {resultado}")
    elif opcao == 4:
        if valor2 != 0:
            resultado = valor1 / valor2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Erro! Não é possível dividir por zero.")
