"""
    1107 : 리모컨
    URL : https://www.acmicpc.net/problem/1107
    Input #1 :
        5457
        3
        6 7 8
    Output #1 :
        6
    Input #2 :
        100
        5
        0 1 2 3 4
    Output #2 :
        0
    Input #3 :
        500000
        8
        0 2 3 4 6 7 8 9
    Output #3 :
        11117
"""

from functools import reduce


def permutation(sequence, m):
    for x in sequence:
        if m == 1:
            yield [x]
        else:
            sub_sequence = sequence.copy()
            for sub_permutation in permutation(sub_sequence, m - 1):
                yield [x] + sub_permutation


def zero_safe_permutation(sequence, m):
    for x in sequence:
        if m == 1:
            yield [x]
        elif x == 0:
            continue
        else:
            sub_sequence = sequence.copy()
            for sub_permutation in permutation(sub_sequence, m - 1):
                yield [x] + sub_permutation


N = input()
M = int(input())
if M > 0:
    unavailable = set(map(int, input().split()))
    available = sorted(list(set(range(10)) - unavailable))
else:
    available = sorted(list(range(10)))

n = int(N)
N = list(map(int, N))
if n > 100:
    count = n - 100
else:
    count = 100 - n

if available:
    upper = None
    upper_as_number = None
    lower = None
    lower_as_number = None

    for p in zero_safe_permutation(available, len(N)):
        i = reduce(lambda x, y: x * 10 + y, p)
        if i >= n:
            upper = p
            upper_as_number = i
            break
        lower = p
        lower_as_number = i

    if upper is None:
        for p in zero_safe_permutation(available, len(N) + 1):
            upper = p
            upper_as_number = reduce(lambda x, y: x * 10 + y, p)
            break

    if (lower is None) and (len(N) > 1):
        reversed_available = available.copy()
        reversed_available.reverse()
        for p in zero_safe_permutation(reversed_available, len(N) - 1):
            lower = p
            lower_as_number = reduce(lambda x, y: x * 10 + y, p)
            break

    if upper:
        count = min(count, len(upper) + upper_as_number - n)
    if lower:
        count = min(count, len(lower) + n - lower_as_number)

print(count)
