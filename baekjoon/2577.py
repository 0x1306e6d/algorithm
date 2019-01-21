"""
    2577 : 숫자의 개수
    URL : https://www.acmicpc.net/problem/2577
    Input :
        150
        266
        427
    Output :
        3
        1
        0
        2
        0
        0
        0
        2
        0
        0
"""

cache = [0 for _ in range(0, 10)]

A = int(input())
B = int(input())
C = int(input())
D = str(A * B * C)

for d in D:
    cache[int(d)] += 1

for i in cache:
    print(i)
