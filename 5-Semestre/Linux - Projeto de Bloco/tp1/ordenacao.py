import time

with open('lista_de_arquivos.txt', 'r') as f:
    files = [line.strip() for line in f.readlines()]

print(f"Total de arquivos carregados: {len(files)}")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

algoritmos = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

for nome, func in algoritmos.items():
    arr = files[:]                    
    inicio = time.time()
    func(arr)
    fim = time.time()
    print(f"{nome}: {fim - inicio:.4f} segundos")