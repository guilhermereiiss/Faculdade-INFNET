import heapq

GRAFO = {
    "Centro": [("Botafogo", 18), ("Tijuca", 16), ("Madureira", 34)],
    "Barra": [("Jacarepagua", 16), ("Ipanema", 32), ("Centro", 40)],
    "Botafogo": [("Copacabana", 10), ("Ipanema", 14), ("Centro", 20)],
    "Copacabana": [("Ipanema", 9), ("Botafogo", 12), ("Centro", 28)],
    "Ipanema": [("Copacabana", 10), ("Botafogo", 16), ("Barra", 30)],
    "Tijuca": [("Centro", 18), ("Madureira", 26), ("Botafogo", 22)],
    "Madureira": [("Tijuca", 30), ("Centro", 35), ("Jacarepagua", 28)],
    "Jacarepagua": [("Barra", 18), ("Madureira", 26)],
}
HUB_A = "Centro"
HUB_B = "Barra"
HUBS = (HUB_A, HUB_B)
ENTREGAS = [
    ("Copacabana", 10, 45, 4),
    ("Ipanema", 25, 75, 5),
    ("Tijuca", 15, 60, 3),
    ("Madureira", 60, 130, 3),
    ("Jacarepagua", 80, 150, 2),
    ("Botafogo", 20, 70, 2),
]


def validar_adjacencias(grafo):
    print("=== Validacao da estrutura do grafo (lista de adjacencia) ===")
    for vertice in ("Centro", "Madureira"):
        print(f"\nVizinhos de {vertice}:")
        for destino, peso in grafo[vertice]:
            print(f"  {vertice} -> {destino} (custo: {peso} min)")


def escolher_hub_inicial():
    justificativa = "Hub escolhido: 'Centro'.\nJustificativa: 4 das 6 entregas (Copacabana, Ipanema, Tijuca e Botafogo) tem janelas que comecam logo no inicio do turno (10, 25, 15 e 20 min). Saindo de 'Centro', o custo direto para Tijuca e de apenas 16 min (cai dentro da janela [15,60]) e para Botafogo e de 18 min (dentro de [20,70]), e a partir desses bairros Copacabana e Ipanema ficam a 10-14 min de distancia. Ja a partir de 'Barra', o unico vizinho diretamente util no inicio e Jacarepagua (16 min), mas essa entrega so abre a janela em t=80, entao o entregador ficaria 64 min esperando ou precisaria de um deslocamento longo (Ipanema a 32 min, Centro a 40 min) para alcancar as entregas com janelas mais cedo. Logo, 'Centro' minimiza o tempo ocioso/deslocamento inicial e atende primeiro as janelas mais restritivas."
    return (HUB_A, justificativa)


def dijkstra(grafo, origem):
    dist = {v: float("inf") for v in grafo}
    prev = {v: None for v in grafo}
    dist[origem] = 0
    heap = [(0, origem)]
    visitados = set()
    while heap:
        d_atual, u = heapq.heappop(heap)
        if u in visitados:
            continue
        visitados.add(u)
        for v, peso in grafo.get(u, []):
            novo_d = d_atual + peso
            if novo_d < dist[v]:
                dist[v] = novo_d
                prev[v] = u
                heapq.heappush(heap, (novo_d, v))
    return (dist, prev)


def construir_tabela_distancias(grafo, pontos_relevantes):
    tabela_dist = {}
    tabela_prev = {}
    for origem in pontos_relevantes:
        dist, prev = dijkstra(grafo, origem)
        tabela_dist[origem] = dist
        tabela_prev[origem] = prev
    return (tabela_dist, tabela_prev)


def travel_cost(u, v, tabela_dist):
    if u not in tabela_dist:
        return None
    custo = tabela_dist[u].get(v, float("inf"))
    return None if custo == float("inf") else custo


def reconstruir_caminho(u, v, tabela_prev):
    if u not in tabela_prev:
        return None
    prev = tabela_prev[u]
    if v != u and prev[v] is None:
        return None
    caminho = []
    atual = v
    while atual is not None:
        caminho.append(atual)
        if atual == u:
            break
        atual = prev[atual]
    caminho.reverse()
    return caminho


PESO_PRIORIDADE = 5
PESO_ATRASO = 3
PESO_URGENCIA = 1
JANELA_URGENCIA = 50


def calcular_score(custo_incremental, prioridade, t_atual, janela_fim):
    slack = janela_fim - (t_atual + custo_incremental)
    atraso_estimado = max(0, -slack)
    folga = max(0, slack)
    bonus_urgencia = max(0, JANELA_URGENCIA - folga)
    return (
        custo_incremental
        - PESO_PRIORIDADE * prioridade
        + PESO_ATRASO * atraso_estimado
        - PESO_URGENCIA * bonus_urgencia
    )


def montar_rota(grafo, hub_inicial, entregas, tabela_dist):
    pendentes = list(entregas)
    t = 0
    local_atual = hub_inicial
    rota = [hub_inicial]
    log = []
    resultado_entregas = []
    while pendentes:
        heap = []
        for idx, (bairro, j_ini, j_fim, prioridade) in enumerate(pendentes):
            custo = travel_cost(local_atual, bairro, tabela_dist)
            if custo is None:
                custo_para_score = float("inf")
                score = float("inf")
            else:
                custo_para_score = custo
                score = calcular_score(custo, prioridade, t, j_fim)
            heapq.heappush(heap, (score, custo_para_score, -prioridade, bairro, idx))
        score, custo, prioridade_neg, bairro, idx = heapq.heappop(heap)
        bairro_sel, j_ini, j_fim, prioridade = pendentes[idx]
        if custo == float("inf"):
            log.append(
                f"ERRO: nao ha caminho de {local_atual} para {bairro_sel}; entrega ignorada."
            )
            pendentes.pop(idx)
            continue
        t_antes = t
        t_chegada = t + custo
        if t_chegada < j_ini:
            espera = j_ini - t_chegada
            t_depois = j_ini
            dentro_janela = True
            atraso = 0
        else:
            espera = 0
            t_depois = t_chegada
            dentro_janela = t_chegada <= j_fim
            atraso = 0 if dentro_janela else t_chegada - j_fim
        status = (
            "DENTRO da janela"
            if dentro_janela
            else f"FORA da janela (atraso de {atraso} min)"
        )
        log.append(
            f"Entrega escolhida: {bairro_sel:12s} | t_antes={t_antes:6.1f} | custo={custo:5.1f} | espera={espera:5.1f} | t_depois={t_depois:6.1f} | janela=[{j_ini},{j_fim}] | status={status}"
        )
        resultado_entregas.append((bairro_sel, t_chegada, dentro_janela, atraso))
        rota.append(bairro_sel)
        t = t_depois
        local_atual = bairro_sel
        pendentes.pop(idx)
    custo_centro = travel_cost(local_atual, HUB_A, tabela_dist)
    custo_barra = travel_cost(local_atual, HUB_B, tabela_dist)
    candidatos = [
        (c, h)
        for c, h in [(custo_centro, HUB_A), (custo_barra, HUB_B)]
        if c is not None
    ]
    custo_retorno, hub_retorno = min(candidatos, key=lambda par: par[0])
    rota.append(hub_retorno)
    t += custo_retorno
    log.append(
        f"Retorno ao hub:      {hub_retorno:12s} | t_antes={t - custo_retorno:6.1f} | custo={custo_retorno:5.1f} | espera={0:5.1f} | t_depois={t:6.1f} | janela=[-,-]  | status=retorno ao hub"
    )
    return (rota, t, log, resultado_entregas)


if __name__ == "__main__":
    validar_adjacencias(GRAFO)
    print("\n=== Escolha do hub inicial ===")
    hub_inicial, justificativa_hub = escolher_hub_inicial()
    print(justificativa_hub)
    pontos_relevantes = set([hub_inicial]) | {e[0] for e in ENTREGAS} | set(HUBS)
    print(f"\nPontos relevantes para Dijkstra: {sorted(pontos_relevantes)}")
    tabela_dist, tabela_prev = construir_tabela_distancias(GRAFO, pontos_relevantes)
    print("\n=== Exemplos de travel_cost ===")
    for u, v in [
        ("Centro", "Madureira"),
        ("Barra", "Tijuca"),
        ("Copacabana", "Jacarepagua"),
    ]:
        c = travel_cost(u, v, tabela_dist)
        caminho = reconstruir_caminho(u, v, tabela_prev)
        print(
            f"travel_cost({u}, {v}) = {c}  | caminho: {(' -> '.join(caminho) if caminho else None)}"
        )
    print("\n=== Log de execucao (heuristica gulosa) ===")
    rota, tempo_total, log, resultado_entregas = montar_rota(
        GRAFO, hub_inicial, ENTREGAS, tabela_dist
    )
    for linha in log:
        print(linha)
    print("\n=== Relatorio final ===")
    print("Rota completa:", " -> ".join(rota))
    print(f"Tempo total do turno: {tempo_total} min (inicio as 09:00)")
    atrasadas = [e for e in resultado_entregas if not e[2]]
    if atrasadas:
        print("\nEntregas FORA da janela:")
        for bairro, chegada, _, atraso in atrasadas:
            print(f"  {bairro}: chegou em t={chegada} min, atraso de {atraso} min")
    else:
        print("\nTodas as entregas foram realizadas dentro da janela.")
    print(
        "\nJustificativa de NP-dificuldade:\nEste problema e uma variante do Vehicle Routing Problem with Time Windows (VRPTW), que generaliza o Problema do Caixeiro Viajante (TSP) -- ja conhecido como NP-dificil -- adicionando janelas de tempo e prioridades. Mesmo com um unico veiculo, encontrar a sequencia de visitas que minimiza o tempo total respeitando todas as janelas e equivalente a um TSP com restricoes de precedencia/tempo, cujo espaco de solucoes (permutacoes das entregas) crece de forma fatorial (O(n!)). Por isso, a busca pela solucao OTIMA exata e inviavel mesmo para poucas dezenas de entregas.\n\nJustificativa da heuristica:\nA heuristica gulosa com heap escolhe, a cada passo, a entrega que minimiza um score combinando custo de deslocamento, prioridade e risco de atraso. Isso tem complexidade O(n^2 log n) no pior caso (n decisoes, cada uma reconstruindo um heap de tamanho O(n)), proxima de linear/quadratica -- muito mais viavel que O(n!). Embora nao garanta o otimo global, a heuristica tende a produzir rotas proximas do ideal porque, em cada decisao local, equilibra distancia, prioridade e urgencia de forma consistente, e o desempate deterministico garante que o mesmo conjunto de entregas sempre produza a mesma rota (reprodutibilidade), facilitando auditoria e testes."
    )
