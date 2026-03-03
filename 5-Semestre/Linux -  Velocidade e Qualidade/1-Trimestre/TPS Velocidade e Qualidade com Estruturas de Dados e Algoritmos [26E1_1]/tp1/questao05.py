def greatestNumber(array):
    if not array:
        return None 

    maior = array[0]

    for numero in array:
        if numero > maior:
            maior = numero

    return maior
