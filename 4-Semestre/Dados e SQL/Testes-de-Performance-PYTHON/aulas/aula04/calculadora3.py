# Calculadora versão 3

def exibir_menu():
    print("----Menu----")
    print("[1] - Somar")
    print("[2] - Subtrair")
    print("[3] - Multiplicar")
    print("[4] - Dividir")

def entrar_operacao():
    operacao = int(input("Entre com a operação: "))
    return operacao

def entrar_operando(msg):
    op = float(input(msg))
    return op

def somar(op1, op2):
    result = op1 + op2
    print("Soma =", result)

def subtrair(op1, op2):
    result = op1 - op2
    print("Subtração =", result)

def multiplicar(op1, op2):
    result = op1 * op2
    print("Multiplicação =", result)

def dividir(op1, op2):
    if (op2 != 0):
        result = op1 / op2
        print("Divisão =", result)
    else:
        print("Erro: divisão por zero")

exibir_menu()
operacao = entrar_operacao()
op1 = entrar_operando("Entre com primeiro operando: ")
op2 = entrar_operando("Entre com segundo operando: ")
match (operacao):
    case 1:
        somar(op1, op2)
    case 2:
        subtrair(op1, op2)
    case 3:
        multiplicar(op1, op2)
    case 4:
        dividir(op1, op2)
    case _:
        print("Erro: operação inválida")