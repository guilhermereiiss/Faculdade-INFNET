def ordena_insercao(valores):
    comp = 0
    mov = 0

    for i in range(1, len(valores)):
        atual = valores[i]
        j = i - 1

        while j >= 0:
            comp += 1
            if valores[j] > atual:
                valores[j+1] = valores[j]
                mov += 1
                j -= 1
            else:
                break

        valores[j+1] = atual

    return valores, comp, mov

print("Quase certo:", ordena_insercao([1, 3, 2, 4, 5, 6]))
print("Ao contrário:", ordena_insercao([10, 9, 8, 7, 6, 5, 4]))