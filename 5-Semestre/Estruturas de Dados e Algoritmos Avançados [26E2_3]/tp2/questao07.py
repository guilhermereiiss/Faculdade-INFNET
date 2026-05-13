class GraphAdjList:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()

    def add_edge(self, u, v, directed=False):
        self.add_vertex(u)
        self.add_vertex(v)

        self.adj[u].add(v)

        if not directed:
            self.adj[v].add(u)

    def print_graph(self):
        for vertex, neighbors in self.adj.items():
            print(vertex, "->", list(neighbors))

    # EX10
    def to_mermaid(self, directed=False):

        result = "graph TD\n"

        visited = set()

        for u in self.adj:
            for v in self.adj[u]:

                if directed:
                    result += f"    {u} --> {v}\n"

                else:
                    edge = tuple(sorted([u, v]))

                    if edge not in visited:
                        visited.add(edge)
                        result += f"    {u} --- {v}\n"

        return result

graph = GraphAdjList()
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E"),
    ("E", "F"),
    ("F", "G"),
    ("G", "H"),
    ("H", "I"),
    ("I", "J"),
    ("J", "A"),
    ("C", "F")
]

for u, v in edges:
    graph.add_edge(u, v)

graph.print_graph()