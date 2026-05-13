
trie_complexity = {
    "insert(word)": "O(n)",
    "search(word)": "O(n)",
    "starts_with(prefix)": "O(n)",
    "autocomplete(prefix, k)": "O(p + s log s)"
}

print("Complexidade da Trie:\n")

for operation, complexity in trie_complexity.items():
    print(f"{operation}: {complexity}")


graph_comparison = {
    "Inserção de aresta": {
        "Lista": "O(1)",
        "Matriz": "O(1)"
    },

    "Consulta de adjacência": {
        "Lista": "O(grau do vértice)",
        "Matriz": "O(1)"
    },

    "Memória": {
        "Lista": "Melhor para grafos esparsos",
        "Matriz": "Melhor para grafos densos"
    }
}

print("\nComparação Lista vs Matriz:\n")

for operation, values in graph_comparison.items():

    print(operation)
    print("Lista:", values["Lista"])
    print("Matriz:", values["Matriz"])
    print()