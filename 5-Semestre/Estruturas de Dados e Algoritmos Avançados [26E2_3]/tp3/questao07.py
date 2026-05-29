from collections import deque

grafo = {
    "Inicio": ["A", "B"],
    "A": ["C"],
    "B": ["C", "F"],
    "C": ["D"],
    "D": ["E"],
    "E": [],
    "F": ["E"]
}

visitados = set()
ordem_dfs = []

def dfs(v):
    visitados.add(v)
    ordem_dfs.append(v)

    for vizinho in grafo[v]:
        if vizinho not in visitados:
            dfs(vizinho)

dfs("Inicio")

print("DFS:", ordem_dfs)


def bfs(origem):
    fila = deque([origem])
    visitados = set([origem])
    ordem = []

    while fila:
        atual = fila.popleft()
        ordem.append(atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return ordem

print("BFS:", bfs("Inicio"))