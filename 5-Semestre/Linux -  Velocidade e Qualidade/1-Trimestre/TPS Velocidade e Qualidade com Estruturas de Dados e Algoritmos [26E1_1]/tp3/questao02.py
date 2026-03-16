import math

def factor(x, lowest=2):
    if x == 0:
        return [0]
    if x == 1:
        return [1]
    if x < 0:
        return [-1] + factor(-x, lowest)

    for i in range(lowest, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return [i] + factor(x // i, i)

    return [x]

print(factor(100))
print(factor(13))
print(factor(-60))