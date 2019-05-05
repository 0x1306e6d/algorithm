"""
    15483 : 최소 편집
    URL : https://www.acmicpc.net/problem/15483
    Input #1 :
        abc
        ab
    Output #1 :
        1
    Input #2 :
        ca
        abc
    Output #2 :
        3
    Input #3 :
        abc
        cba
    Output #3 :
        2
    Input #4 :
        abcd
        bcde
    Output #4 :
        2
    Input #5 :
        abababababa
        aaaaaaaaaaa
    Output #5 :
        5
    Input #6 :
        for
        whileforif
    Output #6 :
        7
    Input #7 :
        whilewhile
        whalewhale
    Output #7 :
        2
    Input #8 :
        aaabaaa
        acacaca
    Output #8 :
        3
    Input #9 :
        qwerty
        dvorak
    Output #9 :
        5
    Input #10 :
        asdf
        asdf
    Output #10 :
        0
"""

import sys
sys.setrecursionlimit(987654321)

MAX_N = 1001

a = input()
b = input()

cache = [[None for _ in range(MAX_N)] for _ in range(MAX_N)]


def lds(ia, ib):
    if (ia >= len(a)) and (ib < len(b)):
        return len(b[ib:])
    elif ib >= len(b):
        return len(a[ia:])

    if cache[ia][ib] is not None:
        return cache[ia][ib]

    if a[ia] == b[ib]:
        cache[ia][ib] = lds(ia + 1, ib + 1)
    else:
        cache[ia][ib] = 1 + min(
            lds(ia + 1, ib), lds(ia, ib + 1), lds(ia + 1, ib + 1)
        )

    return cache[ia][ib]


print(lds(0, 0))
