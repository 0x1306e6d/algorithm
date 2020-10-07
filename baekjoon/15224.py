"""
    File: 15224.py
    Title: EvenOdd
    URL: https://www.acmicpc.net/problem/15224
    Input #1:
        1 127
    Output #1:
        1083
    Input #2:
        74 74
    Output #2:
        11
    Created At: 2020-10-07 22:52:18
"""

MOD = 10**9 + 7


def f(x):
    iterations = 0
    while x != 1:
        if (x % 2) == 0:
            x //= 2
        else:
            x += 1
        iterations += 1
    return iterations % MOD


def s(x):
    if x <= 1:
        return 0
    elif x % 2 == 0:
        return ((x // 2) - 1 + x - 1 + 2 * s(x // 2)) % MOD
    elif x % 2 == 1:
        return (s(x - 1) + f(x)) % MOD


l, r = map(int, input().split())
print((s(r) - s(l - 1)) % MOD)
