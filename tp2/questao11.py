def reverter_string(s):
    pilha = []

    for ch in s:
        pilha.append(ch)

    invertida = ""
    while pilha:
        invertida += pilha.pop()

    return invertida

print(reverter_string("estrutura"))