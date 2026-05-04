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

        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            p = self.parent(i)
            self.operacoes += 1

            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def build_heap(self, array):
        self.heap = array[:]

        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, i):
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

            self.operacoes += 1

            self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
            i = maior

array = [10, 20, 15, 30, 40, 5, 7, 25]
heap1 = BinaryHeap()
for v in array:
    heap1.insert(v)

print("Heap (insert):", heap1.heap)
print("Operacoes (insert):", heap1.operacoes)

heap2 = BinaryHeap()
heap2.build_heap(array)

print("Heap (build):", heap2.heap)
print("Operacoes (build):", heap2.operacoes)