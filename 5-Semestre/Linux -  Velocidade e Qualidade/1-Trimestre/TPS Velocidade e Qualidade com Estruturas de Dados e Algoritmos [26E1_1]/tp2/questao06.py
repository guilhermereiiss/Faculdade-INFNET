def selection_sort(arr):
    comparacoes = 0
    trocas = 0

    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1

    return arr, comparacoes, trocas

print(selection_sort([5,4,3,2,1]))