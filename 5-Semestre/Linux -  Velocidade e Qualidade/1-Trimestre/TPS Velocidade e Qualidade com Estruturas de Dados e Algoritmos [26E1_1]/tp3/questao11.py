def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    if k < len(left):
        return quickselect(left, k)

    elif k == len(left):
        return pivot

    else:
        return quickselect(right, k - len(left) - 1)

arr = [7,2,1,6,8,5,3,4]

print(quickselect(arr, len(arr)//2))