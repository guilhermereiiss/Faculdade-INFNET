import random

n = 20  

a1 = [random.randint(1, 20) for _ in range(n)]
a2 = [random.randint(1, 20) for _ in range(n)]

t1 = [random.randint(1, 10) for _ in range(n-1)]
t2 = [random.randint(1, 10) for _ in range(n-1)]

e1 = random.randint(1, 10)
e2 = random.randint(1, 10)

x1 = random.randint(1, 10)
x2 = random.randint(1, 10)


def linha1(j):
    if j == 0:
        return e1 + a1[0]

    return min(
        linha1(j-1) + a1[j],
        linha2(j-1) + t2[j-1] + a1[j]
    )


def linha2(j):
    if j == 0:
        return e2 + a2[0]

    return min(
        linha2(j-1) + a2[j],
        linha1(j-1) + t1[j-1] + a2[j]
    )

tempo_final = min(
    linha1(n-1) + x1,
    linha2(n-1) + x2
)

print("Tempo minimo:", tempo_final)