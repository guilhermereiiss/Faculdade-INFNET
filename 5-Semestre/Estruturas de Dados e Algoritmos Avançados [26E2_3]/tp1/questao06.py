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

        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            p = self.parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap vazia")

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

            if left < len(self.heap) and self.heap[left] > self.heap[maior]:
                maior = left

            if right < len(self.heap) and self.heap[right] > self.heap[maior]:
                maior = right

            if maior == i:
                break

            self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
            i = maior

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            p = self.parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def contains(self, valor):
        return valor in self.heap

    def delete(self, valor):
        if valor not in self.heap:
            return False

        i = self.heap.index(valor)

        self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
        self.heap.pop()

        if i < len(self.heap):
            if i > 0 and self.heap[i] > self.heap[self.parent(i)]:
                self._heapify_up(i)
            else:
                self._heapify_down(i)

        return True

heap = BinaryHeap()

heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
heap.insert(15)

print("Heap inicial:", heap.heap)

print("Remover 20:", heap.delete(20))
print("Heap:", heap.heap)

print("Remover 99:", heap.delete(99))
print("Heap:", heap.heap)