"""
    17435 : 합성함수와 쿼리
    URL : https://www.acmicpc.net/problem/17435
    Input :
        5
        3 3 5 4 3
        5
        1 1
        2 1
        11 3
        1000 4
        5 1
    Output :
        3
        5
        5
        4
        3
"""

import sys

m = int(input())
f = list(map(int, sys.stdin.readline().split()))

q = int(input())
for _ in range(q):
    n, x = map(int, sys.stdin.readline().split())

    answer = f[x - 1]
    for i in range(n - 1):
        answer = f[answer - 1]

    sys.stdout.write('{}\n'.format(answer))
