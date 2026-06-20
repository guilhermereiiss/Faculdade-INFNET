
rede_microservicos = {
    "Auth": ["Gateway", "Billing"],
    "Gateway": ["Frontend", "MobileApp"],
    "Billing": ["Notification", "Analytics"],
    "Frontend": ["CacheUI"],
    "MobileApp": ["CacheUI", "Logger"],
    "Notification": ["Logger"],
    "Analytics": [],
    "CacheUI": [],
    "Logger": [],
}

def mapear_raio_falha_bfs(grafo, no_inicial):
    visitados = {no_inicial}
    fila = [no_inicial]
    ordem_visitacao = []

    while fila:
        atual = fila.pop(0)         
        ordem_visitacao.append(atual)

        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return ordem_visitacao


def mapear_raio_falha_bfs_com_distancia(grafo, no_inicial):
    visitados = {no_inicial: 0}
    fila = [no_inicial]
    ordem_com_distancia = [(no_inicial, 0)]

    while fila:
        atual = fila.pop(0)
        distancia_atual = visitados[atual]

        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados:
                visitados[vizinho] = distancia_atual + 1
                fila.append(vizinho)
                ordem_com_distancia.append((vizinho, distancia_atual + 1))

    return ordem_com_distancia

def encontrar_cadeia_profunda_dfs(grafo, no_inicial):
    caminho = [no_inicial]
    visitados = {no_inicial}
    atual = no_inicial

    while True:
        proximo = None
        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados:
                proximo = vizinho
                break  

        if proximo is None:
            break  

        caminho.append(proximo)
        visitados.add(proximo)
        atual = proximo

    return caminho

def main():
    no_falho = "Auth"

    print("=" * 65)
    print(f"FALHA DETECTADA NO SERVICO: {no_falho}")
    print("=" * 65)

    ordem_bfs = mapear_raio_falha_bfs(rede_microservicos, no_falho)
    print("\n[1] ORDEM DE MITIGACAO IMEDIATA (BFS)")
    print("Ordem de visitacao:", ordem_bfs)

    print("\nDetalhamento por raio de distancia:")
    ordem_dist = mapear_raio_falha_bfs_com_distancia(rede_microservicos, no_falho)
    raios = {}
    for servico, dist in ordem_dist:
        raios.setdefault(dist, []).append(servico)
    for dist in sorted(raios):
        rotulo = "ponto de falha" if dist == 0 else f"distancia {dist}"
        print(f"  {rotulo:18s}: {raios[dist]}")

    cadeia_dfs = encontrar_cadeia_profunda_dfs(rede_microservicos, no_falho)
    print("\n[2] CAMINHO CRITICO DE DEPENDENCIA (DFS)")
    print("Cadeia mais profunda de colapso:", " -> ".join(cadeia_dfs))
    print(f"Profundidade da cadeia: {len(cadeia_dfs)} servicos")


if __name__ == "__main__":
    main()