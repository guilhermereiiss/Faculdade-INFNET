import random

def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

def k_smallest_A(arr, k):
    return sorted(arr)[:k]

def quick_select_partition(arr, low, high, k):
    if low > high:
        return
    pivot_idx = random.randrange(low, high + 1)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    pi = i + 1
    if pi == k:
        return
    elif pi > k:
        quick_select_partition(arr, low, pi - 1, k)
    else:
        quick_select_partition(arr, pi + 1, high, k)

def k_smallest_B(arr, k):
    if k == 0:
        return []
    a = arr[:]
    quick_select_partition(a, 0, len(a) - 1, k - 1)
    return a[:k]

print("QUESTAO 3: ")
for n in [1000, 10000, 25000, 50000, 100000]:
    arr = [random.randint(0, 1000) for _ in range(n)]
    unique = remove_duplicates(arr)
    k = min(10, len(unique))
    print(f"n={n} unicos={len(unique)}")
    print("  A:", k_smallest_A(unique, k))
    print("  B:", k_smallest_B(unique, k))