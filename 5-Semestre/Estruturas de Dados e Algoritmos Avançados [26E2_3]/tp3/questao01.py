from collections import defaultdict

def dfs(aluno, grafo, visitados):
    visitados.add(aluno)

    for vizinho in grafo[aluno]:
        if vizinho not in visitados:
            dfs(vizinho, grafo, visitados)

def contar_grupos(N, amizades):
    grafo = defaultdict(list)

    for a, b in amizades:
        grafo[a].append(b)
        grafo[b].append(a)

    visitados = set()
    grupos = 0

    for aluno in range(1, N + 1):
        if aluno not in visitados:
            dfs(aluno, grafo, visitados)
            grupos += 1

    return grupos

N = 6
amizades = [
    (1, 2),
    (2, 3),
    (4, 5)
]

print("Numero de grupos:", contar_grupos(N, amizades))