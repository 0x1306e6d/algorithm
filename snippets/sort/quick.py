from random import shuffle

n = int(input())
arr = list(range(n))
shuffle(arr)

print(arr)


def partition(left, right):
    global arr

    middle = (left + right) // 2
    pivot = arr[middle]

    low = left
    high = right
    while low < high:
        while low <= right and arr[low] < pivot:
            low += 1

        while high >= left and arr[high] > pivot:
            high -= 1

        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    return high


def qsort(left, right):
    if left < right:
        middle = partition(left, right)

        qsort(left, middle - 1)
        qsort(middle + 1, right)


qsort(0, n - 1)
print(arr)
