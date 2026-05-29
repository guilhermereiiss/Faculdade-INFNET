import heapq

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

def dijkstra(origem):
    dist = {v: float("inf") for v in grafo}
    dist[origem] = 0

    predecessor = {}

    heap = [(0, origem)]

    while heap:
        custo, atual = heapq.heappop(heap)

        for vizinho, peso in grafo[atual]:
            novo_custo = custo + peso

            if novo_custo < dist[vizinho]:
                dist[vizinho] = novo_custo
                predecessor[vizinho] = atual
                heapq.heappush(heap, (novo_custo, vizinho))

    return dist, predecessor


def reconstruir_caminho(predecessor, origem, destino):
    caminho = []
    atual = destino

    while atual != origem:
        caminho.append(atual)
        atual = predecessor[atual]

    caminho.append(origem)

    caminho.reverse()

    return caminho


distancias, pred = dijkstra("Berco_A")

caminho = reconstruir_caminho(
    pred,
    "Berco_A",
    "Centro_Logistico"
)

print("Caminho mínimo:")
print(caminho)

print("\nCusto total:")
print(distancias["Centro_Logistico"])