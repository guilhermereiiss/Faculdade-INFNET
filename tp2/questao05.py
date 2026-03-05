def primeira_letra_unica(texto):
    contagem = {}
    for letra in texto:
        contagem[letra] = contagem.get(letra, 0) + 1

    for letra in texto:
        if contagem[letra] == 1:
            return letra
    return None


print(primeira_letra_unica("stress"))
print(primeira_letra_unica("aabbccdeeff"))