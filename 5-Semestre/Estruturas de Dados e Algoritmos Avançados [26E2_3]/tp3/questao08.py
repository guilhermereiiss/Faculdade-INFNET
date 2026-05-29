from collections import deque

grafo = {
    "Berco_A": [("Patio_1", 4), ("Patio_2", 7)],
    "Berco_B": [("Patio_2", 3), ("Patio_3", 6)],
    "Patio_1": [("Berco_A", 4), ("Patio_2", 2), ("Alfandega", 8)],
    "Patio_2": [("Berco_A", 7), ("Berco_B", 3),
                ("Patio_1", 2), ("Patio_3", 2),
                ("Alfandega", 5)],
    "Patio_3": [("Berco_B", 6), ("Patio_2", 2),
                ("Centro_Logistico", 4)],
    "Alfandega": [("Patio_1", 8), ("Patio_2", 5),
                  ("Centro_Logistico", 3)],
    "Centro_Logistico": [("Patio_3", 4), ("Alfandega", 3)]
}

def bfs(origem, destino):
    fila = deque([origem])
    visitados = set([origem])
    predecessor = {}

    while fila:
        atual = fila.popleft()

        if atual == destino:
            break

        for vizinho, _ in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                predecessor[vizinho] = atual
                fila.append(vizinho)

    caminho = []
    atual = destino

    while atual != origem:
        caminho.append(atual)
        atual = predecessor[atual]

    caminho.append(origem)
    caminho.reverse()

    return caminho

caminho = bfs("Berco_A", "Centro_Logistico")

print("Caminho:", caminho)

custo = 0

for i in range(len(caminho)-1):
    u = caminho[i]
    v = caminho[i+1]

    for vizinho, peso in grafo[u]:
        if vizinho == v:
            custo += peso

print("Custo total:", custo)