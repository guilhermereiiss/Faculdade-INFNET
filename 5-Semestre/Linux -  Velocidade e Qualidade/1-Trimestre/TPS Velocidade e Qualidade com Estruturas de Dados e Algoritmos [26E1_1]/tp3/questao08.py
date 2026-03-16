memo = {}

def fib_memo(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

print(fib_memo(10))