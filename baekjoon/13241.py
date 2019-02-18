"""
    13241 : 최소공배수
    URL : https://www.acmicpc.net/problem/13241
    Input #1 :
        1 1
    Output #1 :
        1
    Input #2 :
        3 5
    Output #2 :
        15
    Input #3 :
        1 123
    Output #3 :
        123
    Input #4 :
        121 199
    Output #4 :
        24079
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
print(lcm(A, B))
