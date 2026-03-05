def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

print(bubble_sort([5, 3, 8, 4, 2]))
print(bubble_sort([10, -1, 0, 7]))
print(bubble_sort([1, 2, 3, 4]))

print(bubble_sort(["banana", "abacaxi", "laranja", "uva"]))
print(bubble_sort(["zebra", "gato", "cachorro"]))
