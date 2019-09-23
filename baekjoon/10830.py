"""
    10830: 행렬 제곱
    URL: https://www.acmicpc.net/problem/10830
    Input #1:
        2 5
        1 2
        3 4
    Output #1:
        69 558
        337 406
    Input #2:
        3 3
        1 2 3
        4 5 6
        7 8 9
    Output #2:
        468 576 684
        62 305 548
        656 34 412
    Input #3:
        5 10
        1 0 0 0 1
        1 0 0 0 1
        1 0 0 0 1
        1 0 0 0 1
        1 0 0 0 1
    Output #3:
        512 0 0 0 512
        512 0 0 0 512
        512 0 0 0 512
        512 0 0 0 512
        512 0 0 0 512
"""

MOD = 1000

cache = {}


def multiply(a, b, n):
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] = (c[i][j] + ((a[i][k] * b[k][j]) % MOD) % MOD)
    return c


def pow(a, b, n):
    global cache

    if b in cache:
        return cache[b]

    if b == 1:
        cache[b] = a
    elif b == 2:
        cache[b] = multiply(a, a, n)
    else:
        c = b // 2
        d = b - c
        cache[b] = multiply(pow(a, c, n), pow(a, d, n), n)
    return cache[b]


n, b = map(int, input().split())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

c = pow(a, b, n)
for row in c:
    print(' '.join(str(i % MOD) for i in row))
