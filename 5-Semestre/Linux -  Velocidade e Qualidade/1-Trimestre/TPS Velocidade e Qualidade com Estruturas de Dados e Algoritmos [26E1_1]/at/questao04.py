class HashTableChained:
    def __init__(self, capacity=8, load_factor=0.7):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def put(self, key, value):
        if self.size / self.capacity > self.load_factor:
            old = self.buckets
            self.capacity *= 2
            self.buckets = [[] for _ in range(self.capacity)]
            self.size = 0
            for b in old:
                for k, v in b:
                    self.put(k, v)
        idx = hash(key) % self.capacity
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))
        self.size += 1

    def get(self, key):
        idx = hash(key) % self.capacity
        comp = 0
        for k, v in self.buckets[idx]:
            comp += 1
            if k == key:
                return v, comp
        return None, comp

    def delete(self, key):
        idx = hash(key) % self.capacity
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                del self.buckets[idx][i]
                self.size -= 1
                return True
        return False

    def __len__(self):
        return self.size

print("QUESTAO 4: ")
ht = HashTableChained(5)
for i in range(40):
    ht.put(i, i*10)
print("Tamanho:", len(ht), "Capacidade:", ht.capacity)
print("Acessivel apos resize:", all(ht.get(i)[0] == i*10 for i in range(40)))