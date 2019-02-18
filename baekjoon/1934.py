"""
    1934 : 최소공배수
    URL : https://www.acmicpc.net/problem/1934
    Input :
        3
        1 45000
        6 10
        13 17
    Output :
        45000
        30
        221
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


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split(' '))
    print(lcm(A, B))
