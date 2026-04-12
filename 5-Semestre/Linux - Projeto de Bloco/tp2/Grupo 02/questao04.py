import random
import time
import matplotlib.pyplot as plt

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]      
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]     

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(middle):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(middle))


tamanhos = list(range(25, 1001, 25))
tempos = []

for tamanho in tamanhos:
    lista = [random.randint(0, 10000) for _ in range(tamanho)]

    k = random.randint(0, tamanho - 1)

    inicio = time.time()
    quickselect(lista, k)
    fim = time.time()

    tempo_execucao = fim - inicio
    tempos.append(tempo_execucao)

    print(f"Tamanho: {tamanho} | Tempo: {tempo_execucao:.6f} segundos")

plt.plot(tamanhos, tempos)
plt.xlabel("Tamanho da lista")
plt.ylabel("Tempo de execução (s)")
plt.title("QuickSelect - Desempenho")
plt.show()