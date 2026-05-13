class GraphAdjMatrix:
    def __init__(self):
        self.index = {}
        self.mat = []

    def add_vertex(self, v):

        if v in self.index:
            return

        idx = len(self.index)

        self.index[v] = idx

        # adiciona coluna
        for row in self.mat:
            row.append(0)

        # adiciona linha
        self.mat.append([0] * (idx + 1))

    def add_edge(self, u, v, directed=False):

        self.add_vertex(u)
        self.add_vertex(v)

        i = self.index[u]
        j = self.index[v]

        self.mat[i][j] = 1

        if not directed:
            self.mat[j][i] = 1

    def has_edge(self, u, v):

        if u not in self.index or v not in self.index:
            return False

        i = self.index[u]
        j = self.index[v]

        return self.mat[i][j] == 1

    def print_matrix(self):
        for row in self.mat:
            print(row)

matrix_graph = GraphAdjMatrix()

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
    matrix_graph.add_edge(u, v)

matrix_graph.print_matrix()

print(matrix_graph.has_edge("A", "B"))
print(matrix_graph.has_edge("A", "Z"))