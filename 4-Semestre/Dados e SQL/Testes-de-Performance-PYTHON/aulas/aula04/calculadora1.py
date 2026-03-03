# Calculadora versão 1

print("----Menu----")
print("[1] - Somar")
print("[2] - Subtrair")
print("[3] - Multiplicar")
print("[4] - Dividir")
operecao = int(input("Entre com a operação: "))
op1 = float(input("Entre com o operando: "))
op2 = float(input("Entre com o operando: "))
if (operecao == 1):
    result = op1 + op2
    print("Soma =", result)
elif (operecao == 2):
    result = op1 - op2
    print("Subtração =", result)
elif (operecao == 3):
    result = op1 * op2
    print("Multiplicação =", result)
elif (operecao == 4):
    result = op1 / op2
    print("Divisão =", result)
else:
    print("Erro: operação inválida")