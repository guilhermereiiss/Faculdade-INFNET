import time


class HeapMin:
    def __init__(self):
        self.heap = []

    def vazia(self):
        return len(self.heap) == 0

    def inserir(self, item):
        self.heap.append(item)
        self._subir(len(self.heap) - 1)

    def remover_min(self):
        if self.vazia():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimo = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)

        return minimo

    def _subir(self, indice):
        while indice > 0:
            pai = (indice - 1) // 2

            if self.heap[indice][0] < self.heap[pai][0]:
                self.heap[indice], self.heap[pai] = (
                    self.heap[pai],
                    self.heap[indice]
                )
                indice = pai
            else:
                break

    def _descer(self, indice):
        tamanho = len(self.heap)

        while True:
            menor = indice

            esquerda = 2 * indice + 1
            direita = 2 * indice + 2

            if (
                esquerda < tamanho
                and self.heap[esquerda][0] < self.heap[menor][0]
            ):
                menor = esquerda

            if (
                direita < tamanho
                and self.heap[direita][0] < self.heap[menor][0]
            ):
                menor = direita

            if menor == indice:
                break

            self.heap[indice], self.heap[menor] = (
                self.heap[menor],
                self.heap[indice]
            )

            indice = menor


class AgendadorOtimizado:
    def __init__(self):
        self.heap = HeapMin()

    def adicionar_tarefa(
        self,
        id_tarefa: str,
        tempo: int,
        tecnologia: str
    ):
        tarefa = {
            "id": id_tarefa,
            "tempo": tempo,
            "tecnologia": tecnologia
        }

        prioridade_inicial = tempo

        self.heap.inserir(
            (
                prioridade_inicial,
                tempo,
                tecnologia,
                tarefa
            )
        )

    def executar_proxima(
        self,
        tecnologia_atual: str,
        penalidade: int
    ):

        while not self.heap.vazia():

            (
                prioridade,
                tempo,
                tecnologia,
                tarefa
            ) = self.heap.remover_min()

            prioridade_correta = tempo

            if (
                tecnologia_atual is not None
                and tecnologia != tecnologia_atual
            ):
                prioridade_correta += penalidade

            if prioridade != prioridade_correta:

                self.heap.inserir(
                    (
                        prioridade_correta,
                        tempo,
                        tecnologia,
                        tarefa
                    )
                )

                continue

            return tarefa

        return None


tarefas_iniciais = [
    ("T1", 15, "Python"),
    ("T2", 8, "Java"),
    ("T3", 22, "Docker"),
    ("T4", 5, "Java"),
    ("T5", 12, "Python"),
    ("T6", 18, "Docker"),
    ("T7", 4, "C++")
]

agendador = AgendadorOtimizado()

for id_tarefa, tempo, tecnologia in tarefas_iniciais:
    agendador.adicionar_tarefa(
        id_tarefa,
        tempo,
        tecnologia
    )

penalidade_setup = 6
tecnologia_atual = None

print("=== ORDEM DE EXECUCAO ===\n")

while True:

    tarefa = agendador.executar_proxima(
        tecnologia_atual,
        penalidade_setup
    )

    if tarefa is None:
        break

    print(
        f"Tarefa: {tarefa['id']} | "
        f"Tempo: {tarefa['tempo']} | "
        f"Tecnologia: {tarefa['tecnologia']}"
    )

    tecnologia_atual = tarefa["tecnologia"]

print("\n=== TESTE DE DESEMPENHO (50.000 ITENS) ===")

agendador_teste = AgendadorOtimizado()

n = 50000

inicio = time.perf_counter()

for i in range(n):
    agendador_teste.adicionar_tarefa(
        f"T{i}",
        (i % 100) + 1,
        ["Python", "Java", "Docker", "C++"][i % 4]
    )

tecnologia_atual = None
penalidade = 6
tarefas_executadas = 0

while True:

    tarefa = agendador_teste.executar_proxima(
        tecnologia_atual,
        penalidade
    )

    if tarefa is None:
        break

    tecnologia_atual = tarefa["tecnologia"]
    tarefas_executadas += 1

fim = time.perf_counter()

tempo_total = fim - inicio

print(f"\nTeste de desempenho com n={n}")
print(f"Tarefas executadas: {tarefas_executadas}")
print(
    f"Tempo total (adicionar + executar todas): "
    f"{tempo_total:.4f} s"
)

if tempo_total < 0.5:
    print("Requisito (<0.5s): OK")
else:
    print("Requisito (<0.5s): NAO ATENDIDO")