"""
    File: 10164.py
    Title: 격자상의 경로
    URL: https://www.acmicpc.net/problem/10164
    Input #1:
        3 5 8
    Output #1:
        9
    Created At: 2020-08-15 17:50:30
"""

from math import ceil, factorial


def nCr(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


n, m, k = map(int, input().split())

if k == 0 or k == 1 or k == (n * m):
    print(nCr(n + m - 2, n - 1))
elif n == 1 or m == 1:
    print(1)
else:
    if k % m == 0:
        x, y = m, (k // n)
    else:
        x, y = (k % m), ceil(k // n)
    print(nCr(x + y - 2, x - 1) * nCr(m - x + n - y, m - x))
