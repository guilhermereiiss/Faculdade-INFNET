from collections import defaultdict

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

visitados = []
marcados = set()

def dfs(v):
    marcados.add(v)
    visitados.append(v)

    for vizinho in grafo[v]:
        if vizinho not in marcados:
            dfs(vizinho)

dfs("nails")

print("Ordem DFS:")
print(visitados)