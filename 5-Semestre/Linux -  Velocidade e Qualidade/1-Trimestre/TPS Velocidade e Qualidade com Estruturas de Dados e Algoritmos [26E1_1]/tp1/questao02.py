from collections import deque

def ordenar_cartas(cartas):
    A = deque(cartas) 
    B = deque()       
    C = deque()        

    while A:
        x = A.popleft() 

        while B and B[0] < x:
            C.appendleft(B.popleft())

        B.appendleft(x)

        while C:
            B.appendleft(C.popleft())

    return list(B)

cartas = [7, 2, 11, 1, 9, 4, 13, 5, 8, 3, 12, 6, 10]
print(ordenar_cartas(cartas))