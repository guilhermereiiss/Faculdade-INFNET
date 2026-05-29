from collections import deque

grafo = {
    "Idris": ["Kamil", "Talia"],
    "Kamil": ["Idris", "Lina"],
    "Lina": ["Kamil", "Sasha"],
    "Sasha": ["Lina", "Marco"],
    "Marco": ["Sasha", "Ken"],
    "Ken": ["Marco", "Talia"],
    "Talia": ["Idris", "Ken"]
}

def bfs(origem, destino):
    fila = deque([origem])

    visitados = set([origem])

    predecessor = {}

    while fila:
        atual = fila.popleft()

        if atual == destino:
            break

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                predecessor[vizinho] = atual
                fila.append(vizinho)

    # Reconstrução do caminho
    caminho = []
    atual = destino

    while atual != origem:
        caminho.append(atual)
        atual = predecessor[atual]

    caminho.append(origem)
    caminho.reverse()

    return caminho

caminho = bfs("Idris", "Lina")

print("Caminho mínimo:", caminho)
print("Distância:", len(caminho) - 1)