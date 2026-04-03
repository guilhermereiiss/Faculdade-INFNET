from questao04 import HashTableChained

values = [60, 100, 120, 80, 50, 70, 90, 110, 40, 30, 85, 95, 55, 65, 75, 105]
weights = [10, 20, 30, 15, 25, 5, 12, 18, 8, 7, 22, 28, 13, 17, 9, 21]
W = 50
n = len(values)

def knapsack_recursive(i, rem):
    global calls, subproblems
    calls += 1
    subproblems.add((i, rem))
    if i == 0 or rem == 0:
        return 0
    if weights[i-1] > rem:
        return knapsack_recursive(i-1, rem)
    return max(knapsack_recursive(i-1, rem), values[i-1] + knapsack_recursive(i-1, rem - weights[i-1]))

def knapsack_memo(i, rem, memo):
    global calls_memo
    calls_memo += 1
    key = (i, rem)
    cached = memo.get(key)
    if cached is not None:
        return cached[0]
    if i == 0 or rem == 0:
        res = 0
    elif weights[i-1] > rem:
        res = knapsack_memo(i-1, rem, memo)
    else:
        res = max(knapsack_memo(i-1, rem, memo), values[i-1] + knapsack_memo(i-1, rem - weights[i-1], memo))
    memo.put(key, res)
    return res

print("QUESTAO 8: ")
calls = 0
subproblems = set()
v_rec = knapsack_recursive(n, W)
print("Recursivo:", v_rec, "chamadas:", calls)

memo = HashTableChained()
calls_memo = 0
v_mem = knapsack_memo(n, W, memo)
print("Com memoization:", v_mem, "chamadas:", calls_memo)