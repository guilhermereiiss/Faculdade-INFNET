class Stack:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = [None]*capacidade
        self.topo = -1

    def push(self, valor):
        if self.topo == self.capacidade - 1:
            print("Erro: Overflow")
            return
        self.topo += 1
        self.dados[self.topo] = valor

    def pop(self):
        if self.topo == -1:
            print("Erro: Underflow")
            return None
        valor = self.dados[self.topo]
        self.topo -= 1
        return valor

    def estado(self):
        print(self.dados, "Topo:", self.topo)

s = Stack(3)
s.push(10); s.estado()
s.push(20); s.estado()
s.push(30); s.estado()
s.push(40)  # overflow
s.pop(); s.estado()
s.pop(); s.pop(); s.pop()  # underflow