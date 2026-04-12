import random

n = 20

a1 = [random.randint(1, 20) for _ in range(n)]
a2 = [random.randint(1, 20) for _ in range(n)]
a3 = [random.randint(1, 20) for _ in range(n)]

t12 = [random.randint(1, 10) for _ in range(n-1)]  
t13 = [random.randint(1, 10) for _ in range(n-1)]  
t21 = [random.randint(1, 10) for _ in range(n-1)]  
t23 = [random.randint(1, 10) for _ in range(n-1)]  
t31 = [random.randint(1, 10) for _ in range(n-1)]  
t32 = [random.randint(1, 10) for _ in range(n-1)]  

e1 = random.randint(1, 10)
e2 = random.randint(1, 10)
e3 = random.randint(1, 10)


x1 = random.randint(1, 10)
x2 = random.randint(1, 10)
x3 = random.randint(1, 10)

def linha1(j):
    if j == 0:
        return e1 + a1[0]

    return min(
        linha1(j-1) + a1[j],                 
        linha2(j-1) + t21[j-1] + a1[j],      
        linha3(j-1) + t31[j-1] + a1[j]       
    )

def linha2(j):
    if j == 0:
        return e2 + a2[0]

    return min(
        linha2(j-1) + a2[j],                 
        linha1(j-1) + t12[j-1] + a2[j],     
        linha3(j-1) + t32[j-1] + a2[j]       
    )

def linha3(j):
    if j == 0:
        return e3 + a3[0]

    return min(
        linha3(j-1) + a3[j],                 
        linha1(j-1) + t13[j-1] + a3[j],    
        linha2(j-1) + t23[j-1] + a3[j]       
    )

tempo_final = min(
    linha1(n-1) + x1,
    linha2(n-1) + x2,
    linha3(n-1) + x3
)

print("Tempo minimo:", tempo_final)