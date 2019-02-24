"""
    1038 : 감소하는 수
    URL : https://www.acmicpc.net/problem/1038
    Input :
        18
    Output :
        42
"""

from functools import reduce


def permutation(sequence, m):
    for x in sequence:
        if m == 1:
            yield [x]
        else:
            sub_sequence = list(filter(lambda i: i < x, sequence))
            for sub_permutation in permutation(sub_sequence, m - 1):
                yield [x] + sub_permutation


N = int(input())
if N > 1022:
    print(-1)
else:
    n = -1
    cipher = 1
    number = None
    numbers = list(range(10))
    while n < N:
        for p in permutation(numbers, cipher):
            n += 1
            if n == N:
                number = p
                break
        cipher += 1

    print(reduce(lambda x, y: x * 10 + y, number))
