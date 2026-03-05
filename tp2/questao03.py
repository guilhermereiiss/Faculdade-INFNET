def primeiro_duplicado(arr):
    vistos = {}

    for item in arr:
        if item in vistos:
            return item
        vistos[item] = True

print(primeiro_duplicado(["a","b","c","d","b","e"]))