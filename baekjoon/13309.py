"""
    13309 : 트리
    URL : https://www.acmicpc.net/problem/13309
    Input #1 :
        3 4
        1
        1
        2 3 1
        1 3 0
        2 3 1
        1 3 1
    Output #1 :
        YES
        YES
        NO
        NO
    Input #2 :
        11 7
        7
        4
        1
        9
        11
        1
        11
        1
        3
        7
        11 9 1
        8 5 0
        3 9 0
        6 3 1
        10 9 1
        3 10 1
        1 4 1
    Output #2 :
        YES
        NO
        YES
        NO
        NO
        YES
        YES
"""

import sys

n, q = map(int, sys.stdin.readline().split())

parents = [None] * (n + 1)
for i in range(2, n + 1):
    a = int(sys.stdin.readline())
    parents[i] = a

for i in range(q):
    b, c, d = map(int, sys.stdin.readline().split())

    has_path = False
    visited = [False] * (n + 1)

    b_parent = parents[b]
    if b_parent is None:
        b_parent = b
        visited[b_parent] = True
    else:
        while True:
            visited[b_parent] = True

            if parents[b_parent] is not None:
                b_parent = parents[b_parent]
            else:
                break

    c_parent = parents[c]
    if c_parent is None:
        c_parent = c
    else:
        while True:
            if visited[c_parent]:
                has_path = True
                break

            if parents[c_parent] is not None:
                c_parent = parents[c_parent]
            else:
                break

    if not has_path:
        has_path = (b_parent == c_parent)

    if has_path:
        sys.stdout.write('YES\n')
    else:
        sys.stdout.write('NO\n')

    if d == 1:
        if has_path:
            parents[b] = None
        else:
            parents[c] = None
