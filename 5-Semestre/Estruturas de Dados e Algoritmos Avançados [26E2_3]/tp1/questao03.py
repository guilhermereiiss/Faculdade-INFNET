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

heap = BinaryHeap()

print(heap.insert(10)) 
print(heap.insert(20))  
print(heap.insert(5))   
print(heap.insert(30))  

print(heap.heap)  