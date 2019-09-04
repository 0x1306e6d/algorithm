"""
    15650: N과 M (2)
    URL: https://www.acmicpc.net/problem/15650
    Input #1:
        3 1
    Output #1:
        1
        2
        3
    Input #2:
        4 2
    Output #2:
        1 2
        1 3
        1 4
        2 3
        2 4
        3 4
    Input #3:
        4 4
    Output #3:
        1 2 3 4
"""


def permutation(sequence, m, last=0):
    for x in sequence:
        if x < last:
            continue
        if m == 1:
            yield [x]
        else:
            sub_sequence = sequence.copy()
            sub_sequence.remove(x)
            for sub_permutation in permutation(sub_sequence, m - 1, x):
                yield [x] + sub_permutation


n, m = map(int, input().split())
for p in permutation(list(range(1, n + 1)), m):
    print("{}".format(' '.join([str(x) for x in p])))
