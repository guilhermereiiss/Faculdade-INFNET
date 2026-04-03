import random
random.seed(42)

def generate_vector(n):
    return [random.randint(0, n * 10) for _ in range(n)]

def linear_search(arr, target):
    comparisons = 0
    for i, x in enumerate(arr):
        comparisons += 1
        if x == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    comparisons = 0
    for i in range(len(arr) - 1):
        comparisons += 1
        if arr[i] > arr[i + 1]:
            return -1, comparisons
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

print("QUESTAO 1: ")
scales = [102, 1000, 10000, 50000, 100000]

for n in scales:
    arr = generate_vector(n)
    target = arr[n//2] if arr else 0
    print(f"n = {n}")
    pos_l, comp_l = linear_search(arr[:], target)
    sorted_arr = sorted(arr)
    pos_b, comp_b = binary_search(sorted_arr, target)
    print(f"  Linear: posicao={pos_l}, comparacoes={comp_l}")
    print(f"  Binary: posicao={pos_b}, comparacoes={comp_b}")