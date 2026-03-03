def primeiro_nao_repetido(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return None

print(primeiro_nao_repetido("aabbcddeff"))