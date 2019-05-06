"""
    11725 : 트리의 부모 찾기
    URL : https://www.acmicpc.net/problem/11725
    Input #1 :
        7
        1 6
        6 3
        3 5
        4 1
        2 4
        4 7
    Output #1 :
        4
        6
        1
        3
        1
        4
    Input #2 :
        12
        1 2
        1 3
        2 4
        3 5
        3 6
        4 7
        4 8
        5 9
        5 10
        6 11
        6 12
    Output #2 :
        1
        1
        2
        3
        3
        4
        4
        5
        5
        6
        6
"""

import sys
sys.setrecursionlimit((2**31) - 1)

n = int(input())

edges = {}
for i in range(1, n + 1):
    edges[i] = []

for i in range(2, n + 1):
    e1, e2 = map(int, input().split())
    edges[e1].append(e2)
    edges[e2].append(e1)

tree = {}


def build(root):
    global tree

    children = edges[root]
    for child in children:
        if child not in tree:
            tree[child] = root
            build(child)


build(1)
for i in range(2, n + 1):
    print(tree[i])
