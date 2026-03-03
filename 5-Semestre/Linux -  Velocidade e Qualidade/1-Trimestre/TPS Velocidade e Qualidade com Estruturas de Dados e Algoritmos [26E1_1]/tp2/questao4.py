import string

def letra_ausente(texto):
    presente = {c: False for c in string.ascii_lowercase}

    for ch in texto.lower():
        if 'a' <= ch <= 'z':
            presente[ch] = True

    for letra in string.ascii_lowercase:
        if not presente[letra]:
            return letra
        
print(letra_ausente("abcdefghijklmnopqrstuvwxz"))