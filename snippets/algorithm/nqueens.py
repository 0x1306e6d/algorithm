count = 0

n = 8

col = [False] * n
diag1 = [False] * (2 * (n - 1) + 1)
diag2 = [False] * (2 * (n - 1) + 1)


def nqueens(y):
    global count
    if y == n:
        count += 1
        return
    for x in range(n):
        if col[x] or diag1[x + y] or diag2[x + n - y - 1]:
            continue
        col[x] = diag1[x + y] = diag2[x + n - y - 1] = True
        nqueens(y + 1)
        col[x] = diag1[x + y] = diag2[x + n - y - 1] = False


nqueens(0)

print(count)
