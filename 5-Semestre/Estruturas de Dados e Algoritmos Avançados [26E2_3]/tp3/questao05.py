from collections import deque

grafo = {
    "brush": ["nail_polish"],
    "nail_polish": ["brush", "eye_shadow", "nails"],
    "eye_shadow": ["nail_polish", "eye_glasses"],
    "eye_glasses": ["eye_shadow"],
    "nails": ["nail_polish", "pins", "needles", "hammer"],
    "pins": ["nails", "needles"],
    "needles": ["nails", "pins"],
    "hammer": ["nails", "drill", "saw"],
    "drill": ["hammer"],
    "saw": ["hammer", "knife"],
    "knife": ["saw", "fork", "spoon"],
    "fork": ["knife"],
    "spoon": ["knife"]
}

for v in grafo:
    grafo[v].sort()

def bfs(origem):
    fila = deque([origem])
    visitados = set([origem])
    ordem = []

    while fila:
        atual = fila.popleft()
        ordem.append(atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return ordem

print("Ordem BFS:")
print(bfs("nails"))