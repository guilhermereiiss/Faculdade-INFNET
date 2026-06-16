rede_microsservicos = {
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
    ordem = [no_inicial]
    fila = [no_inicial]
    while fila:
        atual = fila.pop(0)
        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                ordem.append(vizinho)
                fila.append(vizinho)
    return ordem


def mapear_raio_falha_bfs_com_distancias(grafo, no_inicial):
    distancia = {no_inicial: 0}
    ordem = [no_inicial]
    fila = [no_inicial]
    while fila:
        atual = fila.pop(0)
        for vizinho in grafo.get(atual, []):
            if vizinho not in distancia:
                distancia[vizinho] = distancia[atual] + 1
                ordem.append(vizinho)
                fila.append(vizinho)
    return (ordem, distancia)


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


if __name__ == "__main__":
    no_falho = "Auth"
    print("=== 1) Ordem de mitigacao imediata (BFS) ===")
    ordem_bfs, distancias = mapear_raio_falha_bfs_com_distancias(
        rede_microsservicos, no_falho
    )
    print("Ordem de visitacao:", ordem_bfs)
    print("\nServicos agrupados por raio (distancia em saltos a partir de Auth):")
    raios = {}
    for servico, dist in distancias.items():
        raios.setdefault(dist, []).append(servico)
    for dist in sorted(raios):
        print(f"  Distancia {dist}: {raios[dist]}")
    print("\n=== 2) Caminho critico de dependencia (DFS) ===")
    cadeia = encontrar_cadeia_profunda_dfs(rede_microsservicos, no_falho)
    print("Cadeia linear mais profunda:", " -> ".join(cadeia))
    print(f"Profundidade (numero de saltos): {len(cadeia) - 1}")
    print(
        f"\nInterpretacao: a partir de Auth, seguindo sempre o primeiro servico dependente listado, a falha se propaga em cadeia direta por {len(cadeia)} servicos antes que o algoritmo precise retroceder para explorar outros ramos (ex.: Billing, Notification/Analytics)."
    )
