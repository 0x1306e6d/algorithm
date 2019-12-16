"""
    17614 : 369
    URL : https://www.acmicpc.net/problem/17614
    Input #1 :
        14
    Output #1 :
        4
    Input #2 :
        36
    Output #2 :
        18
"""

cache = {}


def play(n):
    global cache

    if n in cache:
        return cache[n]

    if n < 10:
        if (n == 3) or (n == 6) or (n == 9):
            return 1
        else:
            return 0

    i = (n // 10)
    j = (n % 10)
    cache[n] = (play(i) + play(j))
    return cache[n]


n = int(input())
count = 0
for i in range(1, n + 1):
    count += play(i)
print(count)
