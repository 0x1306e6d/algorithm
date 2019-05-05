"""
    2903 : 중앙 이동 알고리즘
    URL : https://www.acmicpc.net/problem/2903
    Input :
        1
    Output :
        9
"""

MAX_N = 16

cache = [0 for i in range(MAX_N)]
cache[0] = 2
for i in range(1, MAX_N):
    cache[i] = cache[i - 1] + (cache[i - 1] - 1)

n = int(input())
print(cache[n] ** 2)
