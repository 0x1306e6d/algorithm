"""
    13171 : A
    URL : https://www.acmicpc.net/problem/13171
    Input #1 :
        3
        3
    Output #1 :
        27
    Input #2 :
        100
        100
    Output #2 :
        424090053
"""

MOD = 1000000007

cache = {}


def pow(a, x):
    global cache

    if x == 1:
        return a

    if x in cache:
        return cache[x]

    y = x // 2
    z = x - y
    cache[x] = ((pow(a, y) % MOD) * (pow(a, z) % MOD) % MOD)
    return cache[x]


a = int(input())
x = int(input())
print(pow(a, x))
