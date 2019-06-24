"""
    5692 : 팩토리얼 진법
    URL : https://www.acmicpc.net/problem/5692
    Input :
        719
        1
        15
        110
        102
        0
    Output :
        53
        1
        7
        8
        8
"""

import sys


def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
        yield f


f = list(factorial(9))

while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break

    i = 0
    decimal = 0
    for c in reversed(n):
        decimal += (int(c) * f[i])
        i += 1
    sys.stdout.write("{}\n".format(decimal))
