import heapq
import math

GRAFO = {
    "Centro": [("Botafogo", 18), ("Tijuca", 16), ("Madureira", 34)],
    "Botafogo": [("Copacabana", 10), ("Ipanema", 14), ("Centro", 20)],
    "Copacabana": [("Ipanema", 9), ("Botafogo", 12), ("Centro", 28)],
    "Ipanema": [("Copacabana", 10), ("Botafogo", 16), ("Barra", 30)],
    "Tijuca": [("Centro", 18), ("Madureira", 26), ("Botafogo", 22)],
    "Madureira": [("Tijuca", 30), ("Centro", 35), ("Jacarepagua", 28)],
    "Jacarepagua": [("Barra", 18), ("Madureira", 26)],
    "Barra": [("Jacarepagua", 16), ("Ipanema", 32), ("Centro", 40)],
}

HUB_A = "Centro"
HUB_B = "Barra"

deliveries = [
    ("Copacabana", 10, 45, 4),
    ("Ipanema", 25, 75, 5),
    ("Tijuca", 15, 60, 3),
    ("Madureira", 60, 130, 3),
    ("Jacarepagua", 80, 150, 2),
    ("Botafogo", 20, 70, 2),
]

def imprimir_vizinhos(grafo, nodo):
    vizinhos = grafo.get(nodo, [])
    print(f"Vizinhos de '{nodo}':")
    if not vizinhos:
        print("   (nenhum)")
    for destino, peso in vizinhos:
        print(f"   {nodo} -> {destino}  (peso: {peso} min)")

def dijkstra(grafo, origem):
    dist = {nodo: math.inf for nodo in grafo}
    prev = {nodo: None for nodo in grafo}
    dist[origem] = 0

    heap = [(0, origem)]
    visitados = set()

    while heap:
        d_atual, u = heapq.heappop(heap)
        if u in visitados:
            continue
        visitados.add(u)

        for v, peso in grafo.get(u, []):
            novo_dist = d_atual + peso
            if novo_dist < dist[v]:
                dist[v] = novo_dist
                prev[v] = u
                heapq.heappush(heap, (novo_dist, v))

    return dist, prev

def reconstruir_caminho(prev, origem, destino):
    if prev.get(destino) is None and destino != origem:
        return None
    caminho = [destino]
    atual = destino
    while atual != origem:
        atual = prev[atual]
        if atual is None:
            return None
        caminho.append(atual)
    caminho.reverse()
    return caminho

def calcular_custos_relevantes(grafo, pontos_relevantes):
    dist_matrix = {}
    prev_matrix = {}
    for origem in pontos_relevantes:
        dist, prev = dijkstra(grafo, origem)
        dist_matrix[origem] = dist
        prev_matrix[origem] = prev
    return dist_matrix, prev_matrix

def travel_cost(u, v, dist_matrix, prev_matrix=None, com_caminho=False):
    if u not in dist_matrix:
        return (None, None) if com_caminho else None
    custo = dist_matrix[u].get(v, math.inf)

    if not com_caminho:
        return custo

    if custo == math.inf or prev_matrix is None or u not in prev_matrix:
        return custo, None
    caminho = reconstruir_caminho(prev_matrix[u], u, v)
    return custo, caminho

def escolher_hub_inicial(dist_matrix):
    print("\nComparacao de proximidade dos hubs com as entregas:")
    soma_centro, soma_barra = 0, 0
    for bairro, j_ini, j_fim, prio in deliveries:
        d_centro = dist_matrix[HUB_A].get(bairro, math.inf)
        d_barra = dist_matrix[HUB_B].get(bairro, math.inf)
        soma_centro += d_centro
        soma_barra += d_barra
        print(f"  {bairro:12s} janela [{j_ini:3d},{j_fim:3d}]  "
              f"dist(Centro)={d_centro:5.0f}  dist(Barra)={d_barra:5.0f}")

    print(f"\n  Soma das distancias a partir de Centro: {soma_centro}")
    print(f"  Soma das distancias a partir de Barra : {soma_barra}")

    hub_escolhido = HUB_A if soma_centro <= soma_barra else HUB_B
    print(f"\n  -> Hub escolhido: '{hub_escolhido}'")
    print("  Justificativa: a maioria das entregas (Copacabana, Ipanema,")
    print("  Tijuca, Botafogo) tem janelas que abrem mais cedo (10 a 70 min)")
    print("  e esta mais proxima do Centro; as entregas mais distantes")
    print("  (Madureira, Jacarepagua) tem janelas que abrem mais tarde")
    print("  (60 a 150 min), o que se encaixa naturalmente em uma rota que")
    print("  comeca atendendo a regiao central e so depois avanca para a")
    print("  zona oeste/suburbio.")
    return hub_escolhido

PESO_PRIORIDADE = 10
FATOR_RISCO = 5

def calcular_score(bairro_atual, entrega, t, dist_matrix):
    nome, j_ini, j_fim, prioridade = entrega
    custo = travel_cost(bairro_atual, nome, dist_matrix)

    if custo is None or custo == math.inf:
        return math.inf, custo

    chegada_estimada = t + custo
    if chegada_estimada > j_fim:
        atraso_estimado = chegada_estimada - j_fim
        penalidade_risco = atraso_estimado * FATOR_RISCO
    else:
        penalidade_risco = 0

    score = (-PESO_PRIORIDADE * prioridade) + custo + penalidade_risco
    return score, custo

def executar_heuristica(hub_inicial, deliveries, dist_matrix, prev_matrix):
    pendentes = list(deliveries)
    t = 0
    bairro_atual = hub_inicial
    rota = [hub_inicial]
    log = []
    entregas_fora_da_janela = []

    print("\n" + "=" * 78)
    print("LOG DE EXECUCAO - HEURISTICA GULOSA")
    print("=" * 78)

    while pendentes:
        heap = []
        for entrega in pendentes:
            score, custo = calcular_score(bairro_atual, entrega, t, dist_matrix)
            heapq.heappush(heap, (score, entrega[0], entrega, custo))

        score_escolhido, _, entrega_escolhida, custo = heapq.heappop(heap)
        nome, j_ini, j_fim, prioridade = entrega_escolhida

        if custo == math.inf:
            print(f"  [AVISO] '{nome}' e inalcancavel a partir de "
                  f"'{bairro_atual}'. Pulando entrega.")
            pendentes.remove(entrega_escolhida)
            continue

        t_antes = t
        chegada = t + custo
        if chegada < j_ini:
            espera = j_ini - chegada
            t_depois = j_ini
            status = "DENTRO DA JANELA (com espera)"
        elif chegada <= j_fim:
            espera = 0
            t_depois = chegada
            status = "DENTRO DA JANELA"
        else:
            espera = 0
            t_depois = chegada
            atraso = chegada - j_fim
            status = f"FORA DA JANELA (atraso de {atraso} min)"
            entregas_fora_da_janela.append((nome, chegada, atraso))

        log_linha = (
            f"  Entrega: {nome:12s} | prioridade={prioridade} | "
            f"t_antes={t_antes:6.1f} | custo={custo:5.1f} | espera={espera:5.1f} | "
            f"t_depois={t_depois:6.1f} | {status}"
        )
        print(log_linha)
        log.append(log_linha)

        rota.append(nome)
        bairro_atual = nome
        t = t_depois
        pendentes.remove(entrega_escolhida)

    custo_centro = travel_cost(bairro_atual, HUB_A, dist_matrix)
    custo_barra = travel_cost(bairro_atual, HUB_B, dist_matrix)
    if custo_centro <= custo_barra:
        hub_retorno, custo_retorno = HUB_A, custo_centro
    else:
        hub_retorno, custo_retorno = HUB_B, custo_barra

    t += custo_retorno
    rota.append(hub_retorno)

    print(f"\n  Retorno final: {bairro_atual} -> {hub_retorno} "
          f"(custo: {custo_retorno:.1f} min)")

    return rota, t, entregas_fora_da_janela

def imprimir_relatorio(rota, tempo_total, entregas_fora_da_janela):
    print("\n" + "=" * 78)
    print("RELATORIO FINAL")
    print("=" * 78)
    print("\nRota completa:")
    print("  " + " -> ".join(rota))

    print(f"\nTempo total do turno: {tempo_total:.1f} minutos "
          f"(chegada as {9 + tempo_total // 60:.0f}h{tempo_total % 60:02.0f})")

    print("\nEntregas fora da janela:")
    if not entregas_fora_da_janela:
        print("  Nenhuma. Todas as entregas foram realizadas dentro do prazo.")
    else:
        for nome, chegada, atraso in entregas_fora_da_janela:
            print(f"  - {nome:12s}: chegou em t={chegada:.1f} min "
                  f"(atraso de {atraso:.1f} min)")
        print(
            "\n  Observacao sobre o(s) atraso(s) acima: isso ilustra exatamente a\n"
            "  limitacao esperada de uma heuristica gulosa. Em algum momento da\n"
            "  rota, uma entrega de prioridade mais alta (ex.: Ipanema, prioridade 5)\n"
            "  foi escolhida na frente de uma entrega cuja janela fechava mais cedo,\n"
            "  porque o score deu mais peso a prioridade do que ao risco futuro.\n"
            "  O algoritmo decide olhando apenas para o instante atual - ele nao\n"
            "  reavalia decisoes passadas nem preve o impacto da escolha atual nas\n"
            "  entregas seguintes. Encontrar a ordem que evita esse tipo de atraso\n"
            "  exigiria avaliar combinacoes de rotas, o que nos leva de volta ao\n"
            "  custo exponencial do problema NP-dificil descrito abaixo."
        )

    print("\nJustificativa tecnica (NP-dificuldade e aproximacao):")
    print(
        "  Este problema e uma variacao do Problema do Caixeiro Viajante com\n"
        "  Janelas de Tempo (TSP with Time Windows / VRPTW). O TSP classico ja\n"
        "  e NP-dificil: para visitar N pontos e retornar a origem, existem\n"
        "  (N-1)! ordens possiveis de visitacao, e nao se conhece algoritmo\n"
        "  que resolva o caso geral em tempo polinomial. Adicionar janelas de\n"
        "  horario e prioridades so aumenta a complexidade, pois cada ordem de\n"
        "  visita precisa ser validada contra restricoes de tempo, tornando a\n"
        "  busca exaustiva pela rota otima impraticavel ja com poucas entregas.\n"
        "  Por isso, a heuristica gulosa implementada aqui nao garante a rota\n"
        "  de custo minimo absoluto: ela toma, a cada passo, a decisao local\n"
        "  aparentemente melhor (maior prioridade, menor custo, menor risco de\n"
        "  atraso) sem reavaliar escolhas passadas. Isso resulta em uma solucao\n"
        "  em tempo polinomial (O(K^2 log K) para K entregas, ja que a cada uma\n"
        "  das K iteracoes reconstruimos um heap de ate K elementos), que e\n"
        "  rapida e previsivel o suficiente para uso operacional em tempo real,\n"
        "  mesmo sem a garantia formal de otimalidade."
    )

def main():
    print("=" * 78)
    print("1) MODELAGEM E VALIDACAO DO GRAFO")
    print("=" * 78)
    imprimir_vizinhos(GRAFO, "Centro")
    print()
    imprimir_vizinhos(GRAFO, "Madureira")

    pontos_relevantes = {HUB_A, HUB_B} | {d[0] for d in deliveries}
    print(f"\nPontos relevantes para calculo de custos: {sorted(pontos_relevantes)}")

    dist_matrix, prev_matrix = calcular_custos_relevantes(GRAFO, pontos_relevantes)

    print("\n" + "=" * 78)
    print("2) ESCOLHA DO HUB INICIAL")
    print("=" * 78)
    hub_inicial = escolher_hub_inicial(dist_matrix)

    print("\nExemplo de uso de travel_cost():")
    custo, caminho = travel_cost("Centro", "Jacarepagua", dist_matrix, prev_matrix, com_caminho=True)
    print(f"  travel_cost('Centro', 'Jacarepagua') = {custo} min | caminho: {caminho}")

    rota, tempo_total, fora_da_janela = executar_heuristica(
        hub_inicial, deliveries, dist_matrix, prev_matrix
    )

    imprimir_relatorio(rota, tempo_total, fora_da_janela)

if __name__ == "__main__":
    main()