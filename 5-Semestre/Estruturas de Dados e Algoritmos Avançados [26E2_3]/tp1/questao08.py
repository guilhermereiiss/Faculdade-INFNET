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
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
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

    def build_heap(self, array):
        self.heap = array[:]  

        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

def is_valid_heap(array):
    n = len(array)

    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[i] < array[left]:
            return False

        if right < n and array[i] < array[right]:
            return False

    return True

heap = BinaryHeap()

array1 = [3, 1, 6, 5, 2, 4]
heap.build_heap(array1)
print("Heap 1:", heap.heap)
print("Valida:", is_valid_heap(heap.heap))

array2 = [10, 20, 15, 30, 40, 5, 7, 25]
heap.build_heap(array2)
print("Heap 2:", heap.heap)
print("Valida:", is_valid_heap(heap.heap))