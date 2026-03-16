def mult(x, y):
    if y == 0:
        return 0
    return x + mult(x, y - 1)

# Exemplos:
print(mult(3, 4))   