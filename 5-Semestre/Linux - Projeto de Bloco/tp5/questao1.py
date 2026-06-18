
NUM_CIDADES = 30
CONEXOES = [
    (0, 1, 45, 3), (0, 2, 60, 8), (0, 3, 75, 12), (1, 2, 20, 2), (1, 4, 55, 6),
    (2, 3, 35, 4), (2, 5, 40, 5), (3, 6, 80, 10), (4, 5, 15, 1), (4, 7, 90, 14),
    (5, 6, 30, 3), (5, 8, 50, 7), (6, 9, 65, 9), (7, 8, 25, 2), (7, 10, 70, 11),
    (8, 9, 45, 5), (8, 11, 60, 8), (9, 12, 85, 13), (10, 11, 15, 1), (10, 13, 50, 6),
    (11, 12, 40, 4), (11, 14, 55, 7), (12, 15, 75, 10), (13, 14, 30, 3), (13, 16, 65, 9),
    (14, 15, 35, 4), (14, 17, 45, 6), (15, 18, 90, 15), (16, 17, 20, 2), (16, 19, 55, 8),
    (17, 18, 40, 5), (17, 20, 60, 9), (18, 21, 80, 12), (19, 20, 25, 3), (19, 22, 70, 11),
    (20, 21, 35, 4), (20, 23, 50, 7), (21, 24, 75, 10), (22, 23, 15, 1), (22, 25, 60, 8),
    (23, 24, 45, 6), (23, 26, 55, 7), (24, 27, 90, 14), (25, 26, 30, 3), (25, 28, 65, 9),
    (26, 27, 40, 5), (26, 29, 70, 11), (27, 29, 50, 6), (28, 29, 25, 2), (0, 4, 110, 18),
    (1, 5, 85, 11), (2, 6, 95, 14), (3, 9, 120, 22), (4, 8, 70, 9), (5, 9, 60, 8),
    (6, 12, 110, 16), (7, 11, 65, 9), (8, 12, 80, 11), (9, 15, 130, 24), (10, 14, 55, 7),
    (11, 15, 70, 9), (12, 18, 115, 19), (13, 17, 60, 8), (14, 18, 75, 10), (15, 21, 140, 25),
    (16, 20, 65, 9), (17, 21, 85, 12), (18, 24, 125, 20), (19, 23, 60, 8), (20, 24, 80, 11),
    (21, 27, 135, 23), (22, 26, 55, 7), (23, 27, 75, 10), (24, 29, 110, 17), (0, 7, 200, 35),
    (3, 12, 180, 28), (10, 19, 150, 22), (13, 22, 140, 21), (16, 25, 160, 26), (1, 8, 95, 13),
    (2, 9, 105, 15), (7, 13, 85, 12), (11, 17, 90, 13), (19, 25, 80, 12), (20, 26, 85, 13)
]

class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.pai[x] != x:
            x = self.pai[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.pai[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def kruskal(n, conexoes):
    arestas = list(conexoes)
    tam = len(arestas)
    for i in range(tam):
        for j in range(tam - i - 1):
            if arestas[j][2] > arestas[j + 1][2]:
                arestas[j], arestas[j + 1] = arestas[j + 1], arestas[j]

    uf = UnionFind(n)
    escolhidas = []
    custo = 0

    for origem, destino, c, lat in arestas:
        if uf.union(origem, destino):
            escolhidas.append((origem, destino, c, lat))
            custo += c

    return escolhidas, custo


def dijkstra(n, conexoes, origem):
    adj = [[] for _ in range(n)]
    for o, d, c, lat in conexoes:
        adj[o].append((d, lat))
        adj[d].append((o, lat))

    dist = [float('inf')] * n
    dist[origem] = 0
    visitado = [False] * n

    for _ in range(n):
        u = -1
        menor = float('inf')
        for i in range(n):
            if not visitado[i] and dist[i] < menor:
                menor = dist[i]
                u = i

        if u == -1:
            break
        visitado[u] = True

        for v, peso in adj[u]:
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso

    return dist


mst, custo_total = kruskal(NUM_CIDADES, CONEXOES)

print("REDE DE MENOR CUSTO (Kruskal)")
print()
for o, d, c, lat in mst:
    print(f"{o} - {d}  | custo {c}  | latencia {lat}ms")
print()
print(f"custo total da rede: {custo_total}")

print()
print("LATENCIA A PARTIR DA CIDADE 0 (Dijkstra, rede completa)")
print()
latencias = dijkstra(NUM_CIDADES, CONEXOES, 0)
for cidade in range(1, NUM_CIDADES):
    print(f"cidade 0 -> cidade {cidade}: {latencias[cidade]}ms")
