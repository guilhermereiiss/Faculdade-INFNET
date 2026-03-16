comparisons = 0
copies = 0

def quicksort_inst(arr):
    global comparisons, copies

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for x in arr[:-1]:
        comparisons += 1
        if x <= pivot:
            left.append(x)
            copies += 1
        else:
            right.append(x)
            copies += 1

    result = quicksort_inst(left) + [pivot] + quicksort_inst(right)
    copies += len(result)
    return result

data = [5,3,8,2,1,4]

print(quicksort_inst(data))
print("Comparações:", comparisons)
print("Copias:", copies)