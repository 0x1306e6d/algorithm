"""
    10253 : 헨리
    URL : https://www.acmicpc.net/problem/10253
    Input :
        3
        4 23
        5 7
        8 11
    Output :
        138
        70
        4070
"""


def gcd(a, b):
    if b > a:
        return gcd(b, a)

    if b == 0:
        return a

    if (a % b) == 0:
        return b
    else:
        return gcd(b, a % b)


def smaller(a, b, x):
    return (a * x - b) >= 0


def minus(a, b, x):
    return (a * x - b), (b * x)


def henry(a, b):
    g = gcd(a, b)
    if g != 1:
        a = a // g
        b = b // g

    if a == 1:
        return b

    x = 2
    while True:
        if smaller(a, b, x):
            break
        x += 1

    a, b = minus(a, b, x)
    return henry(a, b)


T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    print(henry(a, b))
