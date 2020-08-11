"""
    File: 1456.py
    Title: 거의 소수
    URL: https://www.acmicpc.net/problem/1456
    Input #1:
        1 1000
    Output #1:
        25
    Created At: 2020-08-11 23:47:30
"""

import math

__MAX__ = 10000001

a, b = map(int, input().split())

sieve = [True] * (__MAX__ + 1)
sieve[0] = False
sieve[1] = False

sqrt_max = int(math.sqrt(__MAX__))
for i in range(2, sqrt_max + 1):
    if sieve[i]:
        for j in range(i * i, __MAX__ + 1, i):
            sieve[j] = False

sqrt_b = int(math.sqrt(b))

count = 0
for i in range(2, sqrt_b + 1):
    if not sieve[i]:
        continue

    j = i * i
    while j <= b:
        if j >= a:
            count += 1
        j *= i

print(count)
