class Queue:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = [None]*capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def enqueue(self, valor):
        if self.tamanho == self.capacidade:
            print("Fila cheia")
            return
        self.dados[self.fim] = valor
        self.fim = (self.fim + 1) % self.capacidade
        self.tamanho += 1

    def dequeue(self):
        if self.tamanho == 0:
            print("Fila vazia")
            return None
        valor = self.dados[self.inicio]
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return valor

    def estado(self):
        print(self.dados, "inicio:", self.inicio, "fim:", self.fim)


fila = Queue(3)

fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
fila.estado()

print("Removido:", fila.dequeue()) 
fila.estado()

fila.enqueue(40)  
fila.estado()

print("Removido:", fila.dequeue())  
print("Removido:", fila.dequeue())  
print("Removido:", fila.dequeue())  

fila.dequeue()  