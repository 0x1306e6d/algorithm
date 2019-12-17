"""
    10974 : 모든 순열
    URL : https://www.acmicpc.net/problem/10974
    Input :
        3
    Output :
        1 2 3
        1 3 2
        2 1 3
        2 3 1
        3 1 2
        3 2 1
"""

import sys


def permutation(sequence):
    if len(sequence) == 1:
        yield [sequence[0]]
    else:
        for i in sequence:
            sub_sequence = sequence.copy()
            sub_sequence.remove(i)
            for p in permutation(sub_sequence):
                yield [i] + p


n = int(sys.stdin.readline())

for p in permutation(list(range(1, n + 1))):
    sys.stdout.write('{}\n'.format(' '.join([str(i) for i in p])))
