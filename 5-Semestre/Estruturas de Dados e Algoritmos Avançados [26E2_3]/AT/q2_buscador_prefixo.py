class NoTrie:
    __slots__ = ("filhos", "fim_de_palavra", "peso")

    def __init__(self):
        self.filhos = {}
        self.fim_de_palavra = False
        self.peso = None


class HeapMinimaTopK:

    def __init__(self, k):
        self.k = k
        self._dados = []

    def __len__(self):
        return len(self._dados)

    @staticmethod
    def _pior_que(a, b):
        peso_a, termo_a = a
        peso_b, termo_b = b
        if peso_a != peso_b:
            return peso_a < peso_b
        return termo_a > termo_b

    def adicionar(self, item):
        if len(self._dados) < self.k:
            self._dados.append(item)
            self._sift_up(len(self._dados) - 1)
        elif self._dados and self._pior_que(self._dados[0], item):
            self._dados[0] = item
            self._sift_down(0)

    def itens(self):
        return list(self._dados)

    def _sift_up(self, i):
        dados = self._dados
        item = dados[i]
        while i > 0:
            pai = i - 1 >> 1
            pai_item = dados[pai]
            if self._pior_que(item, pai_item):
                dados[i] = pai_item
                i = pai
            else:
                break
        dados[i] = item

    def _sift_down(self, i):
        dados = self._dados
        n = len(dados)
        item = dados[i]
        while True:
            esq = 2 * i + 1
            if esq >= n:
                break
            dir_ = esq + 1
            pior_filho = dados[esq]
            pior_idx = esq
            if dir_ < n and self._pior_que(dados[dir_], pior_filho):
                pior_filho = dados[dir_]
                pior_idx = dir_
            if self._pior_que(pior_filho, item):
                dados[i] = pior_filho
                i = pior_idx
            else:
                break
        dados[i] = item


class BuscadorPrefixo:

    def __init__(self):
        self._raiz = NoTrie()

    def inserir_termo(self, termo: str, peso: int):
        no = self._raiz
        for ch in termo:
            if ch not in no.filhos:
                no.filhos[ch] = NoTrie()
            no = no.filhos[ch]
        no.fim_de_palavra = True
        if no.peso is None or peso > no.peso:
            no.peso = peso

    def _localizar_no_prefixo(self, prefixo: str):
        no = self._raiz
        for ch in prefixo:
            if ch not in no.filhos:
                return None
            no = no.filhos[ch]
        return no

    def sugerir_top_k(self, prefixo: str, k: int) -> list:
        if k <= 0:
            return []
        no_prefixo = self._localizar_no_prefixo(prefixo)
        if no_prefixo is None:
            return []
        heap = HeapMinimaTopK(k)
        pilha = [(no_prefixo, prefixo)]
        while pilha:
            no, termo_atual = pilha.pop()
            if no.fim_de_palavra:
                heap.adicionar((no.peso, termo_atual))
            for ch in sorted(no.filhos.keys(), reverse=True):
                pilha.append((no.filhos[ch], termo_atual + ch))
        resultado = heap.itens()
        resultado.sort(key=lambda par: (-par[0], par[1]))
        return [termo for _peso, termo in resultado]


if __name__ == "__main__":
    buscador = BuscadorPrefixo()
    termos = [
        ("smartphone", 100),
        ("smart tv", 80),
        ("smartwatch", 90),
        ("smartwatch", 60),
        ("smartband", 90),
        ("smart home", 70),
        ("celular", 95),
        ("celular gamer", 95),
        ("notebook", 85),
        ("notebook gamer", 88),
    ]
    for termo, peso in termos:
        buscador.inserir_termo(termo, peso)
    print("Top 3 para 'smart':", buscador.sugerir_top_k("smart", 3))
    print("Top 5 para 'smart':", buscador.sugerir_top_k("smart", 5))
    print("Top 2 para 'cel':", buscador.sugerir_top_k("cel", 2))
    print("Top 5 para 'note':", buscador.sugerir_top_k("note", 5))
    print("Top 3 para 'xyz' (inexistente):", buscador.sugerir_top_k("xyz", 3))
    print("\n=== Teste de atualizacao de peso (mantem o maior) ===")
    b2 = BuscadorPrefixo()
    b2.inserir_termo("teste", 10)
    b2.inserir_termo("teste", 5)
    b2.inserir_termo("teste", 20)
    print("Top 1 para 'teste':", b2.sugerir_top_k("teste", 1))
    print("\n=== Teste de performance (volume maior) ===")
    import random
    import string
    import time

    random.seed(7)
    b3 = BuscadorPrefixo()
    n = 20000
    palavras = []
    for _ in range(n):
        tam = random.randint(4, 12)
        palavra = "produto_" + "".join(
            (random.choice(string.ascii_lowercase) for _ in range(tam))
        )
        palavras.append(palavra)
    inicio = time.perf_counter()
    for p in palavras:
        b3.inserir_termo(p, random.randint(1, 1000))
    fim_insercao = time.perf_counter()
    inicio_busca = time.perf_counter()
    top10 = b3.sugerir_top_k("produto_a", 10)
    fim_busca = time.perf_counter()
    print(f"{n} termos inseridos em {fim_insercao - inicio:.4f} s")
    print(f"Top 10 para 'produto_a' calculado em {fim_busca - inicio_busca:.6f} s")
    print("Top 10:", top10)
