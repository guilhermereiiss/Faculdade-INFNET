from collections import defaultdict
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

EDGES = [
    ("Coruña", "Vigo", 171),
    ("Coruña", "Valladolid", 455),
    ("Vigo", "Valladolid", 356),
    ("Oviedo", "Bilbao", 304),
    ("Valladolid", "Bilbao", 280),
    ("Valladolid", "Madrid", 193),
    ("Valladolid", "Zaragoza", 395),
    ("Bilbao", "Zaragoza", 324),
    ("Zaragoza", "Madrid", 325),
    ("Zaragoza", "Barcelona", 296),
    ("Barcelona", "Gerona", 100),
    ("Barcelona", "Valencia", 349),
    ("Madrid", "Valencia", 191),
    ("Valencia", "Murcia", 241),
    ("Madrid", "Albacete", 251),
    ("Albacete", "Murcia", 150),
    ("Madrid", "Badajoz", 403),
    ("Madrid", "Jaén", 335),
    ("Jaén", "Granada", 86),
    ("Jaén", "Sevilla", 242),
    ("Sevilla", "Cádiz", 125),
    ("Sevilla", "Granada", 256),
    ("Granada", "Murcia", 278),
]

CITIES = sorted({c for edge in EDGES for c in edge[:2]})

MAX_DEGREE_DEFAULT = 3
MAX_DEGREE_MADRID = 4


def max_degree(city):
    return MAX_DEGREE_MADRID if city == "Madrid" else MAX_DEGREE_DEFAULT

class UnionFind:
    def __init__(self, elements):
        self.parent = {e: e for e in elements}
        self.rank = {e: 0 for e in elements}

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def build_constrained_mst(edges, cities):
    sorted_edges = merge_sort(edges, key=lambda e: e[2])
    uf = UnionFind(cities)
    degree = {c: 0 for c in cities}
    tree_edges = []

    for u, v, w in sorted_edges:
        if uf.find(u) == uf.find(v):
            continue 
        if degree[u] >= max_degree(u) or degree[v] >= max_degree(v):
            continue  
        uf.union(u, v)
        degree[u] += 1
        degree[v] += 1
        tree_edges.append((u, v, w))

    root = uf.find(cities[0])
    connected = all(uf.find(c) == root for c in cities)

    return tree_edges, degree, connected


def build_adjacency(edge_list):
    adj = defaultdict(list)
    for u, v, w in edge_list:
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj

def bfs_component(adj, start, excluded_edge):
    visited = {start}
    queue = [start]
    while queue:
        node = queue.pop(0)
        for neighbor, _w in adj[node]:
            if frozenset((node, neighbor)) == excluded_edge:
                continue
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def resilience_analysis(tree_edges, all_edges, cities):
    tree_adj = build_adjacency(tree_edges)
    all_set = set(cities)
    results = []

    for (u, v, w) in tree_edges:
        excluded = frozenset((u, v))
        side_u = bfs_component(tree_adj, u, excluded)
        side_v = all_set - side_u

        best_backup = None
        best_cost = None
        for (a, b, cw) in all_edges:
            if frozenset((a, b)) == excluded:
                continue 
            crosses = (a in side_u and b in side_v) or (a in side_v and b in side_u)
            if crosses:
                if best_cost is None or cw < best_cost:
                    best_cost = cw
                    best_backup = (a, b, cw)

        increase = (best_cost - w) if best_backup else None
        results.append({
            "removed_edge": (u, v, w),
            "backup_edge": best_backup,
            "increase": increase,
        })
    return results

def main():
    tree_edges, degree, connected = build_constrained_mst(EDGES, CITIES)
    total_cost = sum(w for _, _, w in tree_edges)

    print("=" * 70)
    print("ÁRVORE GERADORA MÍNIMA COM RESTRIÇÃO DE GRAU")
    print("=" * 70)
    print(f"Cidades conectadas: {len(CITIES)}  |  Conexões na árvore: {len(tree_edges)}")
    print(f"Rede totalmente conectada? {'SIM' if connected else 'NÃO'}\n")

    print("Segmentos selecionados (cidade A - cidade B : custo):")
    for u, v, w in merge_sort(tree_edges, key=lambda e: e[2]):
        print(f"  {u:12s} - {v:12s} : {w}")

    print(f"\nCUSTO TOTAL MÍNIMO DA REDE: {total_cost}")

    print("\nGraus finais por cidade (limite=3, Madrid=4):")
    for c in sorted(degree):
        flag = " <- HUB" if c == "Madrid" else ""
        print(f"  {c:12s}: grau {degree[c]} / máx {max_degree(c)}{flag}")


    print("\n" + "=" * 70)
    print("ANÁLISE DE RESILIÊNCIA — ARESTA CRÍTICA E BACKUP")
    print("=" * 70)

    analysis = resilience_analysis(tree_edges, EDGES, CITIES)

    no_backup = [r for r in analysis if r["backup_edge"] is None]
    with_backup = [r for r in analysis if r["backup_edge"] is not None]

    if no_backup:
        print("\n[!] Conexões SEM alternativa de backup no mapa original")
        print("  (cidades que ficariam isoladas em caso de rompimento):")
        for r in no_backup:
            u, v, w = r["removed_edge"]
            isolated = v if u in ("Madrid",) else u 
            print(f"  - {u} - {v} (custo {w}): nenhuma outra rota disponível")

    if with_backup:
        most_critical = with_backup[0]
        for r in with_backup:
            if r["increase"] > most_critical["increase"]:
                most_critical = r

        u, v, w = most_critical["removed_edge"]
        bu, bv, bw = most_critical["backup_edge"]
        increase = most_critical["increase"]
        new_total = total_cost - w + bw

        print(f"\n[OK] Aresta mais crítica (entre as que possuem backup):")
        print(f"   {u} - {v}  (custo original: {w})")
        print(f"   Impacto do rompimento: aumento de {increase} no custo de reconexão")
        print(f"\n[OK] Aresta de backup recomendada (do mapa original):")
        print(f"   {bu} - {bv}  (custo: {bw})")
        print(f"\n[OK] Novo custo total do sistema após falha + backup: {new_total}")
        print(f"   (custo original {total_cost}  -  removida {w}  +  backup {bw})")

    print("\nDetalhe de todas as arestas da árvore (impacto individual):")
    for r in merge_sort(with_backup, key=lambda r: -r["increase"]):
        u, v, w = r["removed_edge"]
        bu, bv, bw = r["backup_edge"]
        print(f"  {u:10s}-{v:10s} ({w:3d})  ->  backup {bu:10s}-{bv:10s} "
              f"({bw:3d})  | aumento: {r['increase']}")

    plot_network(tree_edges, EDGES, most_critical, with_backup)

    return tree_edges, total_cost, analysis


def plot_network(tree_edges, all_edges, most_critical, with_backup):
    import matplotlib.pyplot as plt
    import networkx as nx

    G = nx.Graph()
    for u, v, w in all_edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42, k=1.3)

    tree_set = {frozenset((u, v)) for u, v, _ in tree_edges}
    critical_edge = frozenset(most_critical["removed_edge"][:2])
    backup_edge = frozenset(most_critical["backup_edge"][:2])

    plt.figure(figsize=(13, 9))

    non_tree_edges = [(u, v) for u, v in G.edges() if frozenset((u, v)) not in tree_set]
    nx.draw_networkx_edges(G, pos, edgelist=non_tree_edges, edge_color="lightgray",
                            style="dashed", width=1)

    tree_edge_list = [(u, v) for u, v, _ in tree_edges
                       if frozenset((u, v)) not in (critical_edge, backup_edge)]
    nx.draw_networkx_edges(G, pos, edgelist=tree_edge_list, edge_color="black", width=2.2)

    nx.draw_networkx_edges(G, pos, edgelist=[tuple(critical_edge)],
                            edge_color="red", width=3.5)
    nx.draw_networkx_edges(G, pos, edgelist=[tuple(backup_edge)],
                            edge_color="green", width=3.5, style="dashed")

    nx.draw_networkx_nodes(G, pos, node_color="#9ecae1", node_size=900, edgecolors="black")
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")

    edge_labels = {(u, v): w for u, v, w in all_edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    plt.title("Rede de Fibra Óptica — Árvore Mínima com Restrição de Grau\n"
              "Vermelho = aresta crítica | Verde tracejado = backup sugerido",
              fontsize=12)
    plt.axis("off")
    plt.tight_layout()
    import os
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "rede_fibra_visualizacao.png")
    plt.savefig(output_path, dpi=150)
    print(f"\n[Gráfico salvo em {output_path}]")


if __name__ == "__main__":
    main()