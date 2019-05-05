"""
    11057 : 오르막 수
    URL : https://www.acmicpc.net/problem/11057
    Input #1 :
        1
    Output #1 :
        10
    Input #2 :
        2
    Output #2 :
        55
    Input #3 :
        3
    Output #3 :
        220
"""

import sys
sys.setrecursionlimit(987654321)

MOD = 10007
MAX_N = 1001
MAX_I = 10

cache = [[None for i in range(MAX_I)] for n in range(MAX_N)]


def up(n, i):
    if cache[n][i] is not None:
        return cache[n][i]

    if n == 1:
        return (9 - i + 1)
    else:
        cache[n][i] = sum([up(n - 1, j) for j in range(i, 10)]) % MOD
        return cache[n][i]


n = int(input())
print(up(n, 0) % MOD)
