"""
    2407 : 조합
    URL : https://www.acmicpc.net/problem/2407
    Input :
        100 6
    Output :
        1192052400
"""

MAX_N = 101
MAX_M = 101

cache = [[-1 for _ in range(MAX_M)] for _ in range(MAX_N)]
cache[0][0] = 1
cache[1][0] = 1
cache[1][1] = 1


def binomial(n, m):
    if m == 0 or m == n:
        return 1

    if cache[n][m] != -1:
        return cache[n][m]

    cache[n][m] = binomial(n - 1, m - 1) + binomial(n - 1, m)
    return cache[n][m]


n, m = map(int, input().split(' '))
print(binomial(n, m))
