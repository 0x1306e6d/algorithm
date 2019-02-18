"""
    3036 : 링
    URL : https://www.acmicpc.net/problem/3036
    Input #1 :
        4
        12 3 8 4
    Output #1 :
        4/1
        3/2
        3/1
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


N = int(input())
rings = list(map(int, input().split(' ')))
for i in range(1, N):
    _gcd = gcd(rings[0], rings[i])
    print("{}/{}".format(rings[0] // _gcd, rings[i] // _gcd))
