import math
def qual_quadrado(quantidade):
    if quantidade <= 0:
        return None
    
    return int(math.log2(quantidade)) + 1

print(qual_quadrado(16))  # 5
print(qual_quadrado(8))   # 4
print(qual_quadrado(1))   # 1
