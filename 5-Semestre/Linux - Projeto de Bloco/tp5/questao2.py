# Questao 2 - bin packing das VMs nos servidores
# next-fit e first-fit decreasing, comparando os dois no final

CAPACIDADE_SERVIDOR = 100

VMS_SOLICITADAS = [
    48, 12, 35, 22, 17, 65, 8, 42, 53, 29,
    14, 38, 47, 19, 25, 61, 33, 9, 55, 23,
    44, 16, 50, 31, 11, 28, 58, 41, 13, 37,
    62, 21, 45, 18, 26, 52, 34, 7, 49, 20,
    39, 15, 57, 32, 12, 27, 54, 43, 10, 36,
    60, 24, 46, 16, 22, 51, 30, 8, 40, 25
]


def next_fit(vms, capacidade):
    servidores = []
    espaco_restante = []

    for vm in vms:
        if servidores and espaco_restante[-1] >= vm:
            servidores[-1].append(vm)
            espaco_restante[-1] -= vm
        else:
            servidores.append([vm])
            espaco_restante.append(capacidade - vm)

    return servidores


def first_fit_decreasing(vms, capacidade):
    # ordena decrescente sem usar sorted/reverse
    vms_ord = list(vms)
    for i in range(len(vms_ord)):
        maior = i
        for j in range(i + 1, len(vms_ord)):
            if vms_ord[j] > vms_ord[maior]:
                maior = j
        vms_ord[i], vms_ord[maior] = vms_ord[maior], vms_ord[i]

    servidores = []
    espaco_restante = []

    for vm in vms_ord:
        colocou = False
        for i in range(len(servidores)):
            if espaco_restante[i] >= vm:
                servidores[i].append(vm)
                espaco_restante[i] -= vm
                colocou = True
                break
        if not colocou:
            servidores.append([vm])
            espaco_restante.append(capacidade - vm)

    return servidores


resultado_nf = next_fit(VMS_SOLICITADAS, CAPACIDADE_SERVIDOR)
resultado_ffd = first_fit_decreasing(VMS_SOLICITADAS, CAPACIDADE_SERVIDOR)

print("=== RESULTADO DA ALOCACAO (HEURISTICAS) ===")

print()
print("[Heuristica Next-Fit]")
print(f"- Servidores utilizados: {len(resultado_nf)} servidores")
print(f"- Exemplo de ocupacao do Servidor 1: {resultado_nf[0]} (Total: {sum(resultado_nf[0])}/{CAPACIDADE_SERVIDOR} GB)")
for i, s in enumerate(resultado_nf, 1):
    print(f"  servidor {i}: {s} -> {sum(s)}/{CAPACIDADE_SERVIDOR}")

print()
print("[Heuristica First-Fit Decreasing]")
print(f"- Servidores utilizados: {len(resultado_ffd)} servidores")
print(f"- Exemplo de ocupacao do Servidor 1: {resultado_ffd[0]} (Total: {sum(resultado_ffd[0])}/{CAPACIDADE_SERVIDOR} GB)")
for i, s in enumerate(resultado_ffd, 1):
    print(f"  servidor {i}: {s} -> {sum(s)}/{CAPACIDADE_SERVIDOR}")

diferenca = len(resultado_nf) - len(resultado_ffd)
print()
print(f"Conclusao: A heuristica First-Fit Decreasing economizou {diferenca} servidores em relacao a Next-Fit.")
