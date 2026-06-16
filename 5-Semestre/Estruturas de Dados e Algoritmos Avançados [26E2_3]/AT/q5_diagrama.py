import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from q5_roteirizacao import (
    GRAFO,
    ENTREGAS,
    HUB_A,
    HUB_B,
    montar_rota,
    construir_tabela_distancias,
    HUBS,
)

pontos = set([HUB_A]) | {e[0] for e in ENTREGAS} | set(HUBS)
tabela_dist, _ = construir_tabela_distancias(GRAFO, pontos)
rota, tempo_total, log, resultado = montar_rota(GRAFO, HUB_A, ENTREGAS, tabela_dist)
pos = {
    "Centro": (0, 1.5),
    "Botafogo": (-0.8, 0.3),
    "Copacabana": (-1.6, -0.8),
    "Ipanema": (-2.8, -1.3),
    "Barra": (-4.8, -1.0),
    "Tijuca": (1.6, 2.8),
    "Madureira": (4.2, 2.0),
    "Jacarepagua": (1.3, -2.2),
}
fig, ax = plt.subplots(figsize=(11, 8))
for u, vizinhos in GRAFO.items():
    for v, peso in vizinhos:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(
                arrowstyle="-|>",
                color="#cccccc",
                lw=1,
                shrinkA=15,
                shrinkB=15,
                connectionstyle="arc3,rad=0.08",
            ),
        )
for i in range(len(rota) - 1):
    u, v = (rota[i], rota[i + 1])
    x1, y1 = pos[u]
    x2, y2 = pos[v]
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="-|>",
            color="#d62728",
            lw=2.5,
            shrinkA=18,
            shrinkB=18,
            connectionstyle=f"arc3,rad={0.18 + 0.02 * i}",
        ),
    )
entregas_dict = {e[0]: e for e in ENTREGAS}
for nome, (x, y) in pos.items():
    if nome in HUBS:
        cor = "#2ca02c"
        marcador = "s"
        tam = 1600
    else:
        cor = "#1f77b4"
        marcador = "o"
        tam = 1600
    ax.scatter(x, y, s=tam, c=cor, edgecolors="black", zorder=3, marker=marcador)
    ax.text(
        x,
        y - 0.32,
        nome,
        ha="center",
        va="top",
        fontsize=10,
        fontweight="bold",
        color="black",
        zorder=4,
    )
for i, nome in enumerate(rota):
    x, y = pos[nome]
    ax.text(
        x + 0.18,
        y + 0.22,
        str(i),
        fontsize=10,
        fontweight="bold",
        color="#d62728",
        zorder=5,
        bbox=dict(boxstyle="circle,pad=0.15", fc="white", ec="#d62728", lw=1),
    )
legenda = [
    mpatches.Patch(color="#2ca02c", label="Hubs (Centro / Barra)"),
    mpatches.Patch(color="#1f77b4", label="Bairros de entrega"),
    mpatches.Patch(color="#d62728", label="Rota executada (ordem numerada)"),
    mpatches.Patch(color="#cccccc", label="Demais arestas do grafo"),
]
ax.set_title(
    f"Rota do entregador - Tempo total: {tempo_total} min (09:00 + {tempo_total} min)\nRota: {' -> '.join(rota)}",
    fontsize=10,
)
ax.set_xlim(-6.0, 5.5)
ax.set_ylim(-3.2, 3.8)
ax.axis("off")
ax.legend(handles=legenda, loc="upper left", fontsize=9, bbox_to_anchor=(0.0, 0.15))
plt.tight_layout()
plt.savefig("/Faculdade/5-Semestre/Estruturas de Dados e Algoritmos Avançados [26E2_3]\AT/q5_rota.png", dpi=150)
print("OK - imagem salva")
