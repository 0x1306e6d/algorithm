"""
    2312 : 수 복원하기
    URL : https://www.acmicpc.net/problem/2312
    Input :
        2
        6
        24
    Output :
        2 1
        3 1
        2 3
        3 1
"""

from math import sqrt

MAX_N = 100001

prime_table = [True for i in range(MAX_N + 1)]
primes = []

prime_table[0] = False
prime_table[1] = False
sqrtn = int(sqrt(MAX_N))
for i in range(2, sqrtn + 1):
    if prime_table[i] is True:
        for j in range(i * i, MAX_N + 1, i):
            prime_table[j] = False

for i, is_prime in enumerate(prime_table):
    if is_prime:
        primes.append(i)

t = int(input())
for tt in range(t):
    n = int(input())
    history = []
    for prime in primes:
        count = 0
        while (n % prime) == 0:
            count += 1
            n = int(n // prime)
        if count > 0:
            history.append((prime, count))
        if n <= 0:
            break
    for factor, count in history:
        print("{} {}".format(factor, count))
