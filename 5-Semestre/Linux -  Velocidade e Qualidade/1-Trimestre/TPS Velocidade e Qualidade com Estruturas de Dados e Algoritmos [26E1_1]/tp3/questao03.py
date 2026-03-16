def power(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    if y < 0:
        return 1 / power(x, -y)

    if y % 2 == 0:
        metade = power(x, y // 2)
        return metade * metade

    return x * power(x, y - 1)

print(power(2, 10))
print(power(5, -2))
print(power(3, 0))