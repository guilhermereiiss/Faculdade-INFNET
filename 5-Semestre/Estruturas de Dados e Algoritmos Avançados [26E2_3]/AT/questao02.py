class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False
        self.peso = 0


class MinHeap:
    def __init__(self, capacidade):
        self.heap = []
        self.capacidade = capacidade

    def tamanho(self):
        return len(self.heap)

    def inserir(self, item):
        if self.tamanho() < self.capacidade:
            self.heap.append(item)
            self._subir(len(self.heap) - 1)
        else:
            if self._eh_melhor(item, self.heap[0]):
                self.heap[0] = item
                self._descer(0)

    def _eh_melhor(self, a, b):
        peso_a, termo_a = a
        peso_b, termo_b = b

        if peso_a > peso_b:
            return True

        if peso_a == peso_b:
            return termo_a < termo_b

        return False

    def remover_min(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)

        return raiz

    def _subir(self, i):
        while i > 0:
            pai = (i - 1) // 2

            if self._menor(self.heap[i], self.heap[pai]):
                self.heap[i], self.heap[pai] = (
                    self.heap[pai],
                    self.heap[i]
                )
                i = pai
            else:
                break

    def _descer(self, i):
        n = len(self.heap)

        while True:
            menor = i

            esq = 2 * i + 1
            dir = 2 * i + 2

            if esq < n and self._menor(
                self.heap[esq],
                self.heap[menor]
            ):
                menor = esq

            if dir < n and self._menor(
                self.heap[dir],
                self.heap[menor]
            ):
                menor = dir

            if menor == i:
                break

            self.heap[i], self.heap[menor] = (
                self.heap[menor],
                self.heap[i]
            )

            i = menor

    def _menor(self, a, b):
        peso_a, termo_a = a
        peso_b, termo_b = b

        if peso_a != peso_b:
            return peso_a < peso_b

        return termo_a > termo_b


class BuscadorPrefixo:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir_termo(self, termo: str, peso: int):
        atual = self.raiz

        for caractere in termo:
            if caractere not in atual.filhos:
                atual.filhos[caractere] = NoTrie()

            atual = atual.filhos[caractere]

        atual.fim_palavra = True

        if peso > atual.peso:
            atual.peso = peso

    def sugerir_top_k(self, prefixo: str, k: int):

        atual = self.raiz

        for caractere in prefixo:
            if caractere not in atual.filhos:
                return []

            atual = atual.filhos[caractere]

        heap = MinHeap(k)

        self._coletar(atual, prefixo, heap)

        resultado = []

        while heap.tamanho() > 0:
            resultado.append(heap.remover_min())

        resultado.sort(
            key=lambda x: (-x[0], x[1])
        )

        return [termo for peso, termo in resultado]

    def _coletar(self, no, palavra_atual, heap):

        if no.fim_palavra:
            heap.inserir(
                (
                    no.peso,
                    palavra_atual
                )
            )

        for caractere, filho in no.filhos.items():
            self._coletar(
                filho,
                palavra_atual + caractere,
                heap
            )

banco_de_palavras = [
    ("teclado", 45),
    ("tecnologia", 90),
    ("tecnico", 75),
    ("tecido", 30),
    ("computacao", 100),
    ("computador", 100),
    ("compilador", 85),
    ("complexo", 85),
    ("componente", 60),
    ("compartilhar", 95),
    ("comunidade", 70),
    ("comunismo", 10),
    ("copo", 40),
    ("carro", 55)
]

buscador = BuscadorPrefixo()

for termo, peso in banco_de_palavras:
    buscador.inserir_termo(termo, peso)

print("Prefixo: comp")
print("Top 5:", buscador.sugerir_top_k("comp", 5))

print()

print("Prefixo: te")
print("Top 3:", buscador.sugerir_top_k("te", 3))

print()

print("Prefixo: comu")
print("Top 2:", buscador.sugerir_top_k("comu", 2))