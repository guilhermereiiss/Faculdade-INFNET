import random

def generate_vector(n, pattern="random"):
    arr = list(range(n))
    
    if pattern == "ordenado":
        return arr
    elif pattern == "reverso":
        return arr[::-1]
    elif pattern == "quase_ordenado":
        arr = list(range(n))
        swaps = max(1, n // 20)
        for _ in range(swaps):
            i = random.randint(0, n-1)
            j = random.randint(0, n-1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    else:  # aleatório
        random.shuffle(arr)
        return arr

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    comparisons = 0
    copies = 0
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                copies += 3
    return a, comparisons, copies

def selection_sort(arr):
    a = arr[:]  
    n = len(a)
    comparisons = 0
    copies = 0
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        # Troca
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            copies += 3
    return a, comparisons, copies

def insertion_sort(arr):
    a = arr[:]  
    n = len(a)
    comparisons = 0
    copies = 0
    
    for i in range(1, n):
        key = a[i]
        copies += 1
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                copies += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        copies += 1
    return a, comparisons, copies

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, val):
    comparisons = 0
    if not root:
        return Node(val), 1
    
    current = root
    while True:
        comparisons += 1
        if val < current.val:
            if current.left is None:
                current.left = Node(val)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = Node(val)
                break
            current = current.right
    return root, comparisons

def inorder_traversal(root, result):
    if not root:
        return 0
    
    stack = []
    current = root
    calls = 0
    
    while stack or current:
        calls += 1
        while current:
            stack.append(current)
            current = current.left
            calls += 1
        
        if stack:
            current = stack.pop()
            result.append(current.val)   
            current = current.right
    
    return calls

def bst_sort(arr):
    root = None
    total_comparisons = 0
    
    for num in arr:
        root, comp = insert_bst(root, num)
        total_comparisons += comp
    
    result = []
    calls = inorder_traversal(root, result)
    
    return result, total_comparisons, calls

def run_question2():
    sizes = [1000, 10000]
    patterns = ["ordenado", "reverso", "quase_ordenado", "aleatorio"]
    algorithms = {
        "Bubble": bubble_sort,
        "Selection": selection_sort,
        "Insertion": insertion_sort,
        "BST": bst_sort
    }
    
    print(f"{'n':>6} {'Padrao':>15} {'Algoritmo':>12} {'Comp. Chaves':>15} {'Copias':>12}")
    print("-" * 70)
    
    for n in sizes:
        for pattern in patterns:
            vec = generate_vector(n, pattern)
            for name, func in algorithms.items():
                _, comp, copies = func(vec)
                print(f"{n:6} {pattern:15} {name:12} {comp:15,} {copies:12,}")


if __name__ == "__main__":
    random.seed(42)
    run_question2()