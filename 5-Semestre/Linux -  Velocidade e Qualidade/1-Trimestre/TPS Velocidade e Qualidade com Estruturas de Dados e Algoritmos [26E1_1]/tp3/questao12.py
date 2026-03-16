from questao09 import quicksort
from questao11 import quickselect
import random

data = [random.randint(1,100) for _ in range(20)]

print("Dados:", data)

ordenado = quicksort(data)
print("QuickSort:", ordenado)

mediana = quickselect(data, len(data)//2)
print("Mediana QuickSelect:", mediana)