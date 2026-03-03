# Calculadora versão 2

print("----Menu----")
print("[1] - Somar")
print("[2] - Subtrair")
print("[3] - Multiplicar")
print("[4] - Dividir")
operacao = int(input("Entre com a operação: "))
op1 = float(input("Entre com o operando: "))
op2 = float(input("Entre com o operando: "))
match (operacao):
    case 1:
        result = op1 + op2
        print("Soma =", result)
    case 2:
        result = op1 - op2
        print("Subtração =", result)
    case 3:
        result = op1 * op2
        print("Multiplicação =", result)
    case 4:
        if (op2 != 0):
            result = op1 / op2
            print("Divisão =", result)
        else:
            print("Erro: divisão por zero")
    case _:
        print("Erro: operação inválida")