"""
    15655 : N과 M (6)
    URL : https://www.acmicpc.net/problem/15655
    Input #1 :
        3 1
        4 5 2
    Output #1 :
        2
        4
        5
    Input #2 :
        4 2
        9 8 7 1
    Output #2 :
        1 7
        1 8
        1 9
        7 8
        7 9
        8 9
    Input #3 :
        4 4
        1231 1232 1233 1234
    Output #3 :
        1231 1232 1233 1234
"""


def permutation(sequence, m, i=0):
    for x in filter(lambda j: j > i, sequence):
        if m == 1:
            yield [x]
        else:
            sub_sequence = sequence.copy()
            sub_sequence.remove(x)
            for sub_permutation in permutation(sub_sequence, m - 1, x):
                yield [x] + sub_permutation


n, m = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
for p in permutation(a, m):
    print(' '.join(str(i) for i in p))
