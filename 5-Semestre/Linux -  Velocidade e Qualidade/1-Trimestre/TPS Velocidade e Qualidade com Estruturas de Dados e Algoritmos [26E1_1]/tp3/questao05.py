def teams(candidates, k, start=0, atual=""):
    if k == 0:
        print(atual)
        return

    for i in range(start, len(candidates)):
        teams(candidates, k - 1, i + 1, atual + candidates[i])

pessoas = "ABCDE"
teams(pessoas, 3)