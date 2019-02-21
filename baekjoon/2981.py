"""
    2981 : 검문
    URL : https://www.acmicpc.net/problem/2981
    Input :
        3
        6
        34
        38
    Output :
        2 4
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


numbers = []

N = int(input())
for _ in range(N):
    numbers.append(int(input()))

numbers = sorted(numbers)

g = numbers[1] - numbers[0]
for i in range(2, len(numbers)):
    g = gcd(g, numbers[i] - numbers[i - 1])

factors = []
for i in range(2, g + 1):
    if (g % i) == 0:
        factors.append(i)
print("{}".format(' '.join([str(x) for x in factors])))
