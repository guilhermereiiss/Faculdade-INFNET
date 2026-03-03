def intersecao_arrays(a, b):
    tabela = {}
    resultado = []

    for elemento in a:
        tabela[elemento] = True

    for elemento in b:
        if elemento in tabela:
            resultado.append(elemento)

    return resultado

a = [1,2,3,4,5,10,20]
b = [3,4,7,10,30]

print(intersecao_arrays(a, b))