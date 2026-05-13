class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # EX1
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    # EX2
    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end

    # EX3
    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True

    # auxiliar
    def _find_node(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return None

            node = node.children[char]

        return node

    # EX4
    def _collect_words(self, node, prefix, words):
        if node.is_end:
            words.append(prefix)

        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)

    # EX5
    def autocomplete(self, prefix, k):
        node = self._find_node(prefix)

        if not node:
            return []

        words = []
        self._collect_words(node, prefix, words)

        words.sort()

        return words[:k]

    # EX6
    def autocorrect(self, word):

        if self.search(word):
            return word

        best_prefix = ""
        best_words = []

        current_prefix = ""

        for char in word:
            current_prefix += char

            node = self._find_node(current_prefix)

            if node:
                best_prefix = current_prefix

                words = []
                self._collect_words(node, current_prefix, words)

                best_words = words
            else:
                break

        if not best_words:
            all_words = []
            self._collect_words(self.root, "", all_words)

            all_words.sort()

            return all_words[0] if all_words else None

        best_words.sort()

        return best_words[0]

trie = Trie()
words = [
    "car",
    "cart",
    "carro",
    "casa",
    "casamento",
    "cat",
    "dog"
]

for word in words:
    trie.insert(word)

# EX1
print(trie.search("car"))      # True
print(trie.search("cart"))     # True

# EX2
print(trie.search("ca"))       # False
print(trie.search("banana"))   # False

# EX3
print(trie.starts_with("cas")) # True
print(trie.starts_with("do"))  # True
print(trie.starts_with("x"))   # False

# EX4
all_words = []
trie._collect_words(trie.root, "", all_words)
print(all_words)

# EX5
print(trie.autocomplete("ca", 3))
print(trie.autocomplete("car", 10))
print(trie.autocomplete("z", 5))

# EX6
print(trie.autocorrect("car"))      # car
print(trie.autocorrect("carr"))     # carro
print(trie.autocorrect("casaa"))    # casa
print(trie.autocorrect("dov"))      # dog
print(trie.autocorrect("zzz"))      # primeira lexicográfica