def desenhar_intervalo(n):
    if n == 0:
        return

    desenhar_intervalo(n - 1)

    print("-" * n)

    desenhar_intervalo(n - 1)

def regua(n):
    print("-" * n)  
    
    for i in range(1, 2**n):
        desenhar_intervalo(n - 1)
        print("-" * n)  

regua(4)