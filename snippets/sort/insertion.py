from random import shuffle

n = int(input())
arr = list(range(n))
shuffle(arr)

print(arr)

for i in range(n):
    k = arr[i]
    index = i
    for j in range(i - 1, -1, -1):
        if arr[j] > k:
            arr[j + 1] = arr[j]
            index = j
        else:
            break
    arr[index] = k

print(arr)
