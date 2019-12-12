"""
    15663 : N과 M (9)
    URL : https://www.acmicpc.net/problem/15663
    Input #1 :
        3 1
        4 4 2
    Output #1 :
        2
        4
    Input #2 :
        4 2
        9 7 9 1
    Output #2 :
        1 7
        1 9
        7 1
        7 9
        9 1
        9 7
        9 9
    Input #3 :
        4 4
        1 1 1 1
    Output #3 :
        1 1 1 1
"""


def permutation(sequence, i):
    last = None
    for x in sequence:
        if last == x:
            continue
        last = x

        if i == 1:
            yield [x]
        else:
            sub_sequence = sequence.copy()
            sub_sequence.remove(x)
            for sub_permutation in permutation(sub_sequence, i - 1):
                yield [x] + sub_permutation


n, m = map(int, input().split())
a = sorted(map(int, input().split()))
for p in permutation(a, m):
    print(' '.join(str(i) for i in p))
