"""
    2609 : 최대공약수와 최소공배수
    URL : https://www.acmicpc.net/problem/2609
    Input #1 :
        24 18
    Output #1 :
        6
        72
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


A, B = map(int, input().split(' '))
print(gcd(A, B))
print(lcm(A, B))
