import time
import random

class BinaryHeap:
    def __init__(self):
        self.heap = []
        self.operacoes = 0  

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, valor):
        self.heap.append(valor)
        i = len(self.heap) - 1

        while i > 0:
            self.operacoes += 1  
            p = self.parent(i)

            if self.heap[p] >= self.heap[i]:
                break

            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            self.operacoes += 1
            i = p

    def extract_max(self):
        if not self.heap:
            return None

        raiz = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        self._heapify_down(0)
        return raiz

    def _heapify_down(self, i):
        while True:
            left = self.left(i)
            right = self.right(i)
            maior = i

            if left < len(self.heap):
                self.operacoes += 1
                if self.heap[left] > self.heap[maior]:
                    maior = left

            if right < len(self.heap):
                self.operacoes += 1
                if self.heap[right] > self.heap[maior]:
                    maior = right

            if maior == i:
                break

            self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
            self.operacoes += 1
            i = maior

    def build_heap(self, array):
        self.heap = array[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

def teste_empirico():
    tamanhos = [100, 500, 1000, 2000, 5000]

    print("n\tinsert_ops\tbuild_ops\ttempo_insert\ttempo_build")

    for n in tamanhos:
        dados = [random.randint(1, 10000) for _ in range(n)]

        heap1 = BinaryHeap()
        inicio = time.time()

        for v in dados:
            heap1.insert(v)

        tempo_insert = time.time() - inicio
        ops_insert = heap1.operacoes

        heap2 = BinaryHeap()
        inicio = time.time()

        heap2.build_heap(dados)

        tempo_build = time.time() - inicio
        ops_build = heap2.operacoes

        print(f"{n}\t{ops_insert}\t{ops_build}\t{tempo_insert:.5f}\t{tempo_build:.5f}")

teste_empirico()