import random
import time

# 1) Versão Quadrática O(N²)

def maior_unico_quadratico(lista):
    comparacoes = 0
    maior = None

    for i in range(len(lista)):
        unico = True
        for j in range(len(lista)):
            comparacoes += 1
            if i != j and lista[i] == lista[j]:
                unico = False
                break

        if unico:
            if maior is None or lista[i] > maior:
                maior = lista[i]

    return maior, comparacoes


# 2) Versão Otimizada O(N) com Hash Table

def maior_unico_hash(lista):
    acessos = 0
    freq = {}

    for num in lista:
        acessos += 1
        freq[num] = freq.get(num, 0) + 1

    maior = None

    for num in lista:
        acessos += 1
        if freq[num] == 1:
            if maior is None or num > maior:
                maior = num

    return maior, acessos


def executar_testes():
    tamanhos = [50, 100, 500, 1000]

    for tamanho in tamanhos:
        lista = list(range(tamanho))
        lista += random.sample(range(tamanho), tamanho // 10)

        print("=" * 60)
        print(f"Tamanho da lista: {len(lista)}")

        # Versão Quadrática
        inicio = time.time()
        resultado_q, comparacoes = maior_unico_quadratico(lista)
        tempo_q = time.time() - inicio

        print("\nVersão Quadrática O(N²)")
        print("Maior número único:", resultado_q)
        print("Comparações realizadas:", comparacoes)
        print("Tempo de execução:", round(tempo_q, 6), "segundos")

        # Versão Hash
        inicio = time.time()
        resultado_h, acessos = maior_unico_hash(lista)
        tempo_h = time.time() - inicio

        print("\nVersão Hash Table O(N)")
        print("Maior número único:", resultado_h)
        print("Acessos realizados:", acessos)
        print("Tempo de execução:", round(tempo_h, 6), "segundos")


if __name__ == "__main__":
    executar_testes()