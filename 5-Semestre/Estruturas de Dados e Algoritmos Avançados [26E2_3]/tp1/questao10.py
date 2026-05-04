class BinaryHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

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

            self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
            i = maior

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap vazia")

        raiz = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)

        return raiz

def top_k(array, k):
    heap = BinaryHeap()
    heap.build_heap(array)

    resultado = []

    for _ in range(min(k, len(array))):
        resultado.append(heap.extract_max())

    return resultado


array = [10, 4, 20, 15, 30, 5, 7]
print(top_k(array, 1))  
print(top_k(array, 3))  
print(top_k(array, 5))  