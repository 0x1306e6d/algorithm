"""
    14490 : 백대열
    URL : https://www.acmicpc.net/problem/14490
    Input #1 :
        100:10
    Output #1 :
        10:1
    Input #2 :
        18:24
    Output #2 :
        3:4
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


n, m = map(int, input().split(':'))
g = gcd(n, m)
print("{}:{}".format(n // g, m // g))
