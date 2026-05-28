
from __future__ import annotations
from typing import Generator

class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False

    def __repr__(self) -> str:
        return (f"TrieNode(is_end={self.is_end}, "
                f"children={list(self.children.keys())})")

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self._size = 0   

    def insert(self, word: str) -> None:
        word = word.lower().strip()
        if not word:
            return
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        if not node.is_end:
            node.is_end = True
            self._size += 1

    def search(self, word: str) -> bool:
        node = self._find_node(word.lower().strip())
        return node is not None and node.is_end

    def remove(self, word: str) -> bool:
        word = word.lower().strip()
        removed = self._remove_recursive(self.root, word, 0)
        if removed:
            self._size -= 1
        return removed

    def _remove_recursive(self, node: TrieNode, word: str, depth: int) -> bool:
        if depth == len(word):
            if not node.is_end:
                return False        
            node.is_end = False
            return True

        ch = word[depth]
        if ch not in node.children:
            return False

        child = node.children[ch]
        removed = self._remove_recursive(child, word, depth + 1)

        if removed and not child.is_end and not child.children:
            del node.children[ch]

        return removed

    def list_words(self) -> list[str]:
        result: list[str] = []
        self._collect(self.root, [], result)
        return sorted(result)

    def _collect(self, node: TrieNode, path: list[str],
                 result: list[str]) -> None:
        if node.is_end:
            result.append("".join(path))
        for ch in sorted(node.children):
            path.append(ch)
            self._collect(node.children[ch], path, result)
            path.pop()

    def autocomplete(self, prefix: str, limit: int = 10) -> list[str]:
        prefix = prefix.lower().strip()
        node = self._find_node(prefix)
        if node is None:
            return []
        result: list[str] = []
        self._collect(node, list(prefix), result)
        return sorted(result)[:limit]

    def autocorrect(self, word: str, max_dist: int = 2,
                    limit: int = 5) -> list[tuple[str, int]]:
        word = word.lower().strip()
        current_row = list(range(len(word) + 1))
        results: list[tuple[str, int]] = []

        for ch, child in self.root.children.items():
            self._search_recursive(child, ch, word, current_row,
                                   results, max_dist)

        results.sort(key=lambda x: (x[1], x[0]))
        return results[:limit]

    def _search_recursive(self, node: TrieNode, letter: str, word: str,
                          prev_row: list[int],
                          results: list[tuple[str, int]],
                          max_dist: int,
                          current_word: str = "") -> None:
        columns = len(word) + 1
        current_row = [prev_row[0] + 1]
        current_word = current_word + letter

        for col in range(1, columns):
            insert_cost  = current_row[col - 1] + 1
            delete_cost  = prev_row[col] + 1
            replace_cost = prev_row[col - 1] + (0 if word[col - 1] == letter else 1)
            current_row.append(min(insert_cost, delete_cost, replace_cost))

        if current_row[-1] <= max_dist and node.is_end:
            results.append((current_word, current_row[-1]))

        if min(current_row) <= max_dist:
            for ch, child in node.children.items():
                self._search_recursive(child, ch, word, current_row,
                                       results, max_dist, current_word)

    def _find_node(self, word: str) -> TrieNode | None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def __len__(self) -> int:
        return self._size

    def __contains__(self, word: str) -> bool:
        return self.search(word)

    def __repr__(self) -> str:
        return f"Trie(size={self._size})"

PORTUGUESE_COMMON_WORDS = [
    "a", "o", "as", "os", "um", "uma", "uns", "umas",
    "de", "do", "da", "dos", "das", "em", "no", "na",
    "nos", "nas", "por", "para", "com", "sem", "até",
    "que", "e", "ou", "mas", "se", "como", "quando",
    "porque", "pois", "porém", "contudo", "entretanto",
    "eu", "tu", "ele", "ela", "nós", "vós", "eles", "elas",
    "me", "te", "se", "lhe", "nos", "vos", "lhes",
    "meu", "minha", "seu", "sua", "nosso", "nossa",
    "isso", "isto", "aquilo", "esse", "esta", "qual",
    "quem", "onde", "quando", "como",
    "ser", "estar", "ter", "haver", "fazer", "poder",
    "querer", "dizer", "saber", "ver", "ir", "vir",
    "dar", "ficar", "falar", "achar", "deixar", "passar",
    "tempo", "dia", "pessoa", "ano", "vez", "coisa",
    "vida", "forma", "parte", "lugar", "casa", "mão",
    "país", "ponto", "governo", "trabalho", "problema",
    "mundo", "homem", "mulher", "criança", "família",
    "cidade", "estado", "direito", "empresa", "água",
    "grande", "pequeno", "bom", "mau", "novo", "velho",
    "primeiro", "último", "mesmo", "próprio", "outro",
    "muito", "mais", "menos", "bem", "também", "já",
    "ainda", "só", "não", "sim", "aqui", "lá", "então",
    "sempre", "nunca", "talvez", "certamente",
    "escola", "saúde", "cultura", "música", "livro",
    "número", "sistema", "projeto", "processo",
]

def run_tests():
    print("\n" + "="*60)
    print("  QUESTÃO 2 - TRIE: BATERIA DE TESTES")
    print("="*60)

    trie = Trie()

    print("\n[1] Inserindo palavras do corpus...")
    for w in PORTUGUESE_COMMON_WORDS:
        trie.insert(w)
    print(f"    Total de palavras inseridas: {len(trie)}")
    assert len(trie) >= 100, "Deveria ter >= 100 palavras"

    print("\n[2] Busca exata:")
    tests_search = [("casa", True), ("vida", True), ("xyz123", False),
                    ("Car", False), ("grande", True)]
    all_ok = True
    for word, expected in tests_search:
        result = trie.search(word)
        status = "OK" if result == expected else "XX"
        if result != expected:
            all_ok = False
        print(f"    {status} search('{word}') = {result}  (esperado={expected})")
    print(f"    Resultado: {'PASSOU' if all_ok else 'FALHOU'}")

    print("\n[3] Remoção:")
    trie.insert("computador")
    assert trie.search("computador"), "Deveria encontrar 'computador'"
    removed = trie.remove("computador")
    assert removed and not trie.search("computador"), "Remoção falhou"
    print("    OK 'computador' inserido e removido com sucesso")
    removed_again = trie.remove("computador")
    assert not removed_again
    print("    OK Remoção de palavra inexistente retorna False")

    print("\n[4] Listagem (primeiras 20):")
    words = trie.list_words()
    print(f"    {words[:20]}")
    print(f"    Total listado: {len(words)}")

    print("\n[5] Autocomplete:")
    for prefix in ["ca", "pr", "es", "mu"]:
        suggestions = trie.autocomplete(prefix)
        print(f"    autocomplete('{prefix}') -> {suggestions}")

    print("\n[6] Autocorrect (distância <= 2):")
    for typo in ["caza", "vidda", "homem", "muzica", "eztar"]:
        suggestions = trie.autocorrect(typo, max_dist=2)
        print(f"    autocorrect('{typo}') -> {suggestions}")

    print("\n[7] Inserção de duplicata:")
    before = len(trie)
    trie.insert("casa")
    after = len(trie)
    assert before == after, "Duplicata não deveria aumentar o tamanho"
    print(f"    OK Tamanho antes={before}, depois={after} (sem mudança)")

    print("\n[8] Autocomplete com prefixo inexistente:")
    result = trie.autocomplete("zzz")
    print(f"    autocomplete('zzz') -> {result}  (esperado=[])")
    assert result == []

    print("\n" + "="*60)
    print("  TODOS OS TESTES CONCLUÍDOS COM SUCESSO")
    print("="*60)

if __name__ == "__main__":
    run_tests()
