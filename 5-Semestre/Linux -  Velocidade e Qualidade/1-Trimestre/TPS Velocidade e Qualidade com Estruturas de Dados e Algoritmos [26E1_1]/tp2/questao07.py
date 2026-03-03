def insertion_sort(arr):
    comparacoes = 0
    deslocamentos = 0

    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1
            if arr[j] > chave:
                arr[j+1] = arr[j]
                deslocamentos += 1
                j -= 1
            else:
                break

        arr[j+1] = chave

    return arr, comparacoes, deslocamentos

print("Quase ordenado:", insertion_sort([1,2,3,5,4,6]))
print("Invertido:", insertion_sort([6,5,4,3,2,1]))