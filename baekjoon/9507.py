"""
    9507 : Generations of Tribbles
    URL : https://www.acmicpc.net/problem/9507
    Input :
        8
        0
        1
        2
        3
        4
        5
        30
        67
    Output :
        1
        1
        2
        4
        8
        15
        201061985
        7057305768232953720
"""

MAX_N = 68
cache = [-1 for _ in range(MAX_N)]
cache[0] = 1
cache[1] = 1
cache[2] = 2
cache[3] = 4


def koong(n):
    if cache[n] != -1:
        return cache[n]

    cache[n] = koong(n - 1) + koong(n - 2) + koong(n - 3) + koong(n - 4)
    return cache[n]


T = int(input())
for _ in range(T):
    n = int(input())
    print(koong(n))
