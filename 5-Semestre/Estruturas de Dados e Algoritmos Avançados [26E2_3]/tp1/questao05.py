class BinaryHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, valor):
        self.heap.append(valor)
        i = len(self.heap) - 1
        trocas = []

        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            p = self.parent(i)
            trocas.append((self.heap[p], self.heap[i]))
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

        return trocas

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap vazia")

        raiz = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        i = 0
        passos = []

        while True:
            left = self.left(i)
            right = self.right(i)
            maior = i

            if left < len(self.heap) and self.heap[left] > self.heap[maior]:
                maior = left

            if right < len(self.heap) and self.heap[right] > self.heap[maior]:
                maior = right

            if maior == i:
                break

            passos.append(self.heap.copy())

            self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
            i = maior

        return raiz, passos

    def contains(self, valor):
        for elemento in self.heap:
            if elemento == valor:
                return True
        return False

heap = BinaryHeap()

heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)

print(heap.heap)      

print(heap.contains(20))  
print(heap.contains(99))  