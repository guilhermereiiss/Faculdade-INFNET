class HeapMinima:

    def __init__(self):
        self._dados = []

    def __len__(self):
        return len(self._dados)

    def vazio(self):
        return len(self._dados) == 0

    def inserir(self, item):
        self._dados.append(item)
        self._sift_up(len(self._dados) - 1)

    def remover_minimo(self):
        if not self._dados:
            raise IndexError("remover_minimo() chamado em heap vazia")
        raiz = self._dados[0]
        ultimo = self._dados.pop()
        if self._dados:
            self._dados[0] = ultimo
            self._sift_down(0)
        return raiz

    def _sift_up(self, i):
        dados = self._dados
        item = dados[i]
        while i > 0:
            pai = i - 1 >> 1
            pai_item = dados[pai]
            if item < pai_item:
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
            menor_filho = dados[esq]
            menor_idx = esq
            if dir_ < n and dados[dir_] < menor_filho:
                menor_filho = dados[dir_]
                menor_idx = dir_
            if menor_filho < item:
                dados[i] = menor_filho
                i = menor_idx
            else:
                break
        dados[i] = item


class AgendadorOtimizado:

    def __init__(self):
        self._heap = HeapMinima()
        self._contador = 0
        self.ultima_tecnologia = None

    def adicionar_tarefa(self, id_tarefa: str, tempo: int, tecnologia: str):
        prioridade_inicial = tempo
        item = (prioridade_inicial, self._contador, id_tarefa, tempo, tecnologia)
        self._contador += 1
        self._heap.inserir(item)

    def executar_proxima(self, tecnologia_atual: str, penalidade: int) -> str:
        while not self._heap.vazio():
            prioridade, ordem, id_tarefa, tempo, tecnologia = (
                self._heap.remover_minimo()
            )
            if tecnologia == tecnologia_atual:
                prioridade_real = tempo
            else:
                prioridade_real = tempo + penalidade
            if prioridade_real == prioridade:
                self.ultima_tecnologia = tecnologia
                return id_tarefa
            novo_item = (prioridade_real, ordem, id_tarefa, tempo, tecnologia)
            self._heap.inserir(novo_item)
        return None

    def vazio(self) -> bool:
        return self._heap.vazio()


if __name__ == "__main__":
    print("=== Teste funcional simples ===")
    ag = AgendadorOtimizado()
    ag.adicionar_tarefa("T1", 10, "Python")
    ag.adicionar_tarefa("T2", 4, "Java")
    ag.adicionar_tarefa("T3", 5, "Python")
    ag.adicionar_tarefa("T4", 6, "Docker")
    tecnologia_atual = "Python"
    penalidade = 5
    ordem_execucao = []
    while not ag.vazio():
        proxima = ag.executar_proxima(tecnologia_atual, penalidade)
        ordem_execucao.append(proxima)
        tecnologia_atual = ag.ultima_tecnologia
    print("Ordem de execucao:", ordem_execucao)
    print()
    print("=== Teste de performance: 50.000 tarefas ===")
    import random
    import time

    random.seed(42)
    tecnologias = ["Python", "Java", "Docker", "Go", "Rust", "C++"]
    ag2 = AgendadorOtimizado()
    n = 50000
    inicio_insercao = time.perf_counter()
    for i in range(n):
        ag2.adicionar_tarefa(
            f"T{i}", random.randint(1, 1000), random.choice(tecnologias)
        )
    fim_insercao = time.perf_counter()
    tecnologia_atual = "Python"
    penalidade = 50
    inicio_exec = time.perf_counter()
    total_executadas = 0
    while not ag2.vazio():
        proxima = ag2.executar_proxima(tecnologia_atual, penalidade)
        tecnologia_atual = ag2.ultima_tecnologia
        total_executadas += 1
    fim_exec = time.perf_counter()
    print(f"Tarefas inseridas: {n}")
    print(f"Tarefas executadas: {total_executadas}")
    print(f"Tempo de insercao: {fim_insercao - inicio_insercao:.4f} s")
    print(f"Tempo de execucao (executar_proxima x {n}): {fim_exec - inicio_exec:.4f} s")
    print(f"Tempo total: {fim_exec - inicio_insercao:.4f} s")
