"""
    1850 : 최대공약수
    URL : https://www.acmicpc.net/problem/1850
    Input #1 :
        3 4
    Output #1 :
        1
    Input #2 :
        3 6
    Output #2 :
        111
    Input #3 :
        500000000000000000 500000000000000002
    Output #3 :
        11
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


A, B = map(int, input().split(' '))
print('1' * gcd(A, B))
