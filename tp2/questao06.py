def ordena_selecao(itens):
    qtd_comp = 0
    qtd_troca = 0

    n = len(itens)
    for i in range(n):
        menor = i
        for j in range(i+1, n):
            qtd_comp += 1
            if itens[j] < itens[menor]:
                menor = j

        if menor != i:
            itens[i], itens[menor] = itens[menor], itens[i]
            qtd_troca += 1

    return itens, qtd_comp, qtd_troca


print(ordena_selecao([5,4,3,2,1]))