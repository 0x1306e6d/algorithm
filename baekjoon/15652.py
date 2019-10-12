"""
    15652 : N과 M (4)
    URL : https://www.acmicpc.net/problem/15652
    Input #1 :
        3 1
    Output #1 :
        1
        2
        3
    Input #2 :
        4 2
    Output #2 :
        1 1
        1 2
        1 3
        1 4
        2 2
        2 3
        2 4
        3 3
        3 4
        4 4
    Input #3 :
        3 3
    Output #3 :
        1 1 1
        1 1 2
        1 1 3
        1 2 2
        1 2 3
        1 3 3
        2 2 2
        2 2 3
        2 3 3
        3 3 3
"""


def permutation(sequence, m, i=0):
    for x in filter(lambda j: j >= i, sequence):
        if m == 1:
            yield [x]
        else:
            for sub_permutation in permutation(sequence, m - 1, x):
                yield [x] + sub_permutation


n, m = map(int, input().split())
for p in permutation(list(range(1, n + 1)), m):
    print(' '.join(str(i) for i in p))
