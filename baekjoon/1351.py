"""
    1351 : 무한 수열
    URL : https://www.acmicpc.net/problem/1351
    Input :
        7 2 3
    Output :
        7
"""

cache = {}
n, p, q = map(int, input().split())


def a(i):
    if i == 0:
        return 1
    elif i in cache:
        return cache[i]
    else:
        cache[i] = a(i // p) + a(i // q)
        return cache[i]


print(a(n))
