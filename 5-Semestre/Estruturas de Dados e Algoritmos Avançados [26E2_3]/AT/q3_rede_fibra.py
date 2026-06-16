ARESTAS = [
    ("Coruna", "Vigo", 171),
    ("Coruna", "Valladolid", 455),
    ("Vigo", "Valladolid", 356),
    ("Oviedo", "Bilbao", 304),
    ("Valladolid", "Bilbao", 280),
    ("Valladolid", "Madrid", 193),
    ("Bilbao", "Madrid", 395),
    ("Bilbao", "Zaragoza", 324),
    ("Zaragoza", "Madrid", 325),
    ("Zaragoza", "Barcelona", 296),
    ("Barcelona", "Gerona", 100),
    ("Madrid", "Barcelona", 349),
    ("Madrid", "Badajoz", 403),
    ("Madrid", "Jaen", 335),
    ("Madrid", "Albacete", 251),
    ("Albacete", "Valencia", 191),
    ("Albacete", "Murcia", 150),
    ("Murcia", "Valencia", 241),
    ("Jaen", "Granada", 86),
    ("Murcia", "Granada", 278),
    ("Sevilha", "Jaen", 242),
    ("Sevilha", "Granada", 256),
    ("Sevilha", "Cadiz", 125),
]
GRAU_MAXIMO_PADRAO = 3
GRAU_MAXIMO_MADRID = 4


def limite_grau(cidade: str) -> int:
    return GRAU_MAXIMO_MADRID if cidade == "Madrid" else GRAU_MAXIMO_PADRAO


class UnionFind:

    def __init__(self, elementos):
        self._pai = {e: e for e in elementos}
        self._rank = {e: 0 for e in elementos}

    def encontrar(self, x):
        while self._pai[x] != x:
            self._pai[x] = self._pai[self._pai[x]]
            x = self._pai[x]
        return x

    def unir(self, x, y) -> bool:
        rx, ry = (self.encontrar(x), self.encontrar(y))
        if rx == ry:
            return False
        if self._rank[rx] < self._rank[ry]:
            rx, ry = (ry, rx)
        self._pai[ry] = rx
        if self._rank[rx] == self._rank[ry]:
            self._rank[rx] += 1
        return True


def todos_vertices(arestas):
    vertices = set()
    for u, v, _ in arestas:
        vertices.add(u)
        vertices.add(v)
    return vertices


def construir_mst_com_grau_limitado(arestas):
    vertices = todos_vertices(arestas)
    dsu = UnionFind(vertices)
    grau = {v: 0 for v in vertices}
    arestas_ordenadas = sorted(arestas, key=lambda a: a[2])
    arvore = []

    def tentar_adicionar(u, v, c):
        if dsu.encontrar(u) == dsu.encontrar(v):
            return False
        if grau[u] + 1 > limite_grau(u):
            return False
        if grau[v] + 1 > limite_grau(v):
            return False
        dsu.unir(u, v)
        grau[u] += 1
        grau[v] += 1
        arvore.append((u, v, c))
        return True

    pendentes = []
    for u, v, c in arestas_ordenadas:
        if not tentar_adicionar(u, v, c):
            pendentes.append((u, v, c))
    mudou = True
    while mudou and len(arvore) < len(vertices) - 1:
        mudou = False
        ainda_pendentes = []
        for u, v, c in pendentes:
            if tentar_adicionar(u, v, c):
                mudou = True
            else:
                ainda_pendentes.append((u, v, c))
        pendentes = ainda_pendentes
    custo_total = sum((c for _, _, c in arvore))
    conectado = len(arvore) == len(vertices) - 1
    return (arvore, custo_total, conectado, grau)


def componente_apos_remocao(arvore, aresta_removida, vertices):
    u_rem, v_rem, _ = aresta_removida
    adjacencia = {v: [] for v in vertices}
    for u, v, c in arvore:
        if (u, v, c) == aresta_removida:
            continue
        adjacencia[u].append(v)
        adjacencia[v].append(u)
    visitados = {u_rem}
    fila = [u_rem]
    while fila:
        atual = fila.pop()
        for viz in adjacencia[atual]:
            if viz not in visitados:
                visitados.add(viz)
                fila.append(viz)
    return visitados


def encontrar_backup(aresta_removida, arvore, todas_arestas, vertices):
    componente_u = componente_apos_remocao(arvore, aresta_removida, vertices)
    melhor = None
    for u, v, c in todas_arestas:
        if (u, v, c) == aresta_removida:
            continue
        em_u = u in componente_u
        em_v = v in componente_u
        if em_u != em_v:
            if melhor is None or c < melhor[2]:
                melhor = (u, v, c)
    return melhor


def analisar_aresta_critica(arvore, custo_total, todas_arestas, vertices):
    melhor_impacto = -1
    aresta_critica = None
    backup_da_critica = None
    for aresta in arvore:
        backup = encontrar_backup(aresta, arvore, todas_arestas, vertices)
        if backup is None:
            impacto = float("inf")
        else:
            impacto = backup[2] - aresta[2]
        if impacto > melhor_impacto:
            melhor_impacto = impacto
            aresta_critica = aresta
            backup_da_critica = backup
    if backup_da_critica is None:
        novo_custo = float("inf")
    else:
        novo_custo = custo_total - aresta_critica[2] + backup_da_critica[2]
    return (aresta_critica, backup_da_critica, melhor_impacto, novo_custo)


if __name__ == "__main__":
    vertices = todos_vertices(ARESTAS)
    arvore, custo_total, conectado, grau = construir_mst_com_grau_limitado(ARESTAS)
    print("=== Rede principal (MST com restricao de grau) ===")
    print(f"Total de cidades: {len(vertices)}")
    print(f"Arestas selecionadas ({len(arvore)} de {len(vertices) - 1} necessarias):")
    for u, v, c in sorted(arvore, key=lambda a: -a[2]):
        print(f"  {u} -- {v} : {c}")
    print(f"Custo total minimo: {custo_total}")
    print(f"Rede totalmente conectada? {('SIM' if conectado else 'NAO')}")
    print("\nGraus finais por cidade (limite=3, Madrid=4):")
    for cidade in sorted(vertices):
        print(f"  {cidade:12s}: grau={grau[cidade]} (limite={limite_grau(cidade)})")
    print("\n=== Analise de resiliencia (aresta critica / backup) ===")
    aresta_critica, backup, impacto, novo_custo = analisar_aresta_critica(
        arvore, custo_total, ARESTAS, vertices
    )
    u, v, c = aresta_critica
    print(f"Aresta mais critica: {u} -- {v} (custo {c})")
    if backup:
        bu, bv, bc = backup
        print(f"Aresta de backup sugerida: {bu} -- {bv} (custo {bc})")
        print(f"Impacto (aumento de custo se {u}--{v} falhar): {impacto}")
        print(f"Novo custo total da rede apos a falha + backup: {novo_custo}")
    else:
        print(
            "Nenhuma aresta de backup disponivel no mapa original (rede ficaria desconectada nesse cenario)."
        )
