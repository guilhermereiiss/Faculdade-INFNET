class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def _find_node(self, prefix):

        node = self.root

        for char in prefix:

            if char not in node.children:
                return None

            node = node.children[char]

        return node

    def _collect_words(self, node, prefix, words):

        if node.is_end:
            words.append(prefix)

        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)

    def autocomplete(self, prefix, k):

        node = self._find_node(prefix)

        if not node:
            return []

        words = []

        self._collect_words(node, prefix, words)

        words.sort()

        return words[:k]

class GraphAdjList:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):

        if v not in self.adj:
            self.adj[v] = set()

    def add_edge(self, u, v):

        self.add_vertex(u)
        self.add_vertex(v)

        self.adj[u].add(v)
        self.adj[v].add(u)

def find_vertices_by_prefix(prefix, k, trie, graph):

    candidates = trie.autocomplete(prefix, k)

    result = []

    for word in candidates:

        if word in graph.adj:
            result.append(word)

    return result


# TESTE

vertices = [
    "auth",
    "api",
    "cache",
    "cart",
    "catalog",
    "payment",
    "profile"
]

# cria trie
trie = Trie()

for v in vertices:
    trie.insert(v)

# cria grafo
graph = GraphAdjList()

for v in vertices:
    graph.add_vertex(v)

# cria conexões
graph.add_edge("auth", "api")
graph.add_edge("api", "cache")
graph.add_edge("cart", "catalog")
graph.add_edge("payment", "profile")

# consultas
print(find_vertices_by_prefix("ca", 10, trie, graph))
print(find_vertices_by_prefix("a", 10, trie, graph))
print(find_vertices_by_prefix("p", 10, trie, graph))