def on3(arr):
    best = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sum = 0
            for k in range(i, j):
                sum += arr[k]
            best = max(best, sum)
    return best


def on2(arr):
    best = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i + 1, len(arr)):
            sum += arr[j]
            best = max(best, sum)
    return best


def on1(arr):
    best, sum = 0, 0
    for a in arr:
        sum = max(sum + a, a)
        best = max(best, sum)
    return best


arr = [-1, 2, 4, -3, 5, 2, -5, 2]
print(on3(arr))
print(on2(arr))
print(on1(arr))
