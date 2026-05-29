from collections import defaultdict, deque

def bfs(inicio, destino, grafo):
    fila = deque([inicio])
    visitados = set([inicio])

    while fila:
        atual = fila.popleft()

        if atual == destino:
            return True

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return False


def contar_passeios_validos(S, tuneis, passeios):
    grafo = defaultdict(list)

    for x, y in tuneis:
        grafo[x].append(y)
        grafo[y].append(x)

    validos = 0

    for passeio in passeios:
        possivel = True

        for i in range(len(passeio) - 1):
            if not bfs(passeio[i], passeio[i + 1], grafo):
                possivel = False
                break

        if possivel:
            validos += 1

    return validos


S = 5
tuneis = [(1,2), (2,3), (4,5)]

passeios = [
    [1,3],
    [1,5],
    [4,5]
]

print(contar_passeios_validos(S, tuneis, passeios))