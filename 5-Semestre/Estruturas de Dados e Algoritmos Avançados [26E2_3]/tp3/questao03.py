from collections import defaultdict, deque

def bfs(origem, destino, grafo):
    fila = deque([origem])
    visitados = set([origem])

    while fila:
        atual = fila.popleft()

        if atual == destino:
            return True

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return False


def processar_operacoes(N, operacoes):
    grafo = defaultdict(list)

    for tipo, a, b in operacoes:

        if tipo == 1:
            grafo[a].append(b)
            grafo[b].append(a)

        else:
            print(1 if bfs(a, b, grafo) else 0)


operacoes = [
    (1, 1, 2),
    (1, 2, 3),
    (0, 1, 3),
    (0, 1, 4)
]

processar_operacoes(4, operacoes)