"""
    17175 : 피보나치는 지겨웡~
    URL : https://www.acmicpc.net/problem/17175
    Input #1 :
        2
    Output #1 :
        3
    Input #2 :
        3
    Output #2 :
        5
"""

MOD = 1000000007

cache = {}


def fibonacci(n):
    global cache

    if n in cache:
        return cache[n]
    elif n < 2:
        cache[n] = n
    else:
        cache[n] = fibonacci(n - 2) + fibonacci(n - 1)

    return cache[n]


n = int(input())
if n < 2:
    print(1)
else:
    fibonacci(n)
    print((sum(cache.values()) + cache[n - 1]) % MOD)
