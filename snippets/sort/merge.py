from random import shuffle

n = int(input())
arr = list(range(n))
shuffle(arr)

print(arr)

temp = [0] * n


def merge(left, mid, right):
    global n
    global arr
    global temp

    i = left
    j = mid + 1
    k = left
    while (i <= mid) and (j <= right):
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    if i <= mid:
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
    else:
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]


def msort(left, right):
    if left < right:
        mid = (left + right) // 2

        msort(left, mid)
        msort(mid + 1, right)

        merge(left, mid, right)


msort(0, n - 1)
print(arr)
