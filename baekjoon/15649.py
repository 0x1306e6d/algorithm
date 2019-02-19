"""
    15649 : N과 M (1)
    URL : https://www.acmicpc.net/problem/15649
    Input #1 :
        3 1
    Output #1 :
        1
        2
        3
    Input #2 :
        4 2
    Output #2 :
        1 2
        1 3
        1 4
        2 1
        2 3
        2 4
        3 1
        3 2
        3 4
        4 1
        4 2
        4 3
    Input #3 :
        4 4
    Output #3 :
        1 2 3 4
        1 2 4 3
        1 3 2 4
        1 3 4 2
        1 4 2 3
        1 4 3 2
        2 1 3 4
        2 1 4 3
        2 3 1 4
        2 3 4 1
        2 4 1 3
        2 4 3 1
        3 1 2 4
        3 1 4 2
        3 2 1 4
        3 2 4 1
        3 4 1 2
        3 4 2 1
        4 1 2 3
        4 1 3 2
        4 2 1 3
        4 2 3 1
        4 3 1 2
        4 3 2 1
"""


def permutation(sequence, m):
    for x in sequence:
        if m == 1:
            yield [x]
        else:
            sub_sequence = sequence.copy()
            sub_sequence.remove(x)
            for sub_permutation in permutation(sub_sequence, m - 1):
                yield [x] + sub_permutation


N, M = map(int, input().split(' '))
for p in permutation(list(range(1, N + 1)), M):
    print("{}".format(' '.join([str(x) for x in p])))
