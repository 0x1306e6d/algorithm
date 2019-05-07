"""
    1289 : 트리의 가중치
    URL : https://www.acmicpc.net/problem/1289
    Input #1 :
        3
        3 2 100
        2 1 100
    Output #1 :
        10200
    Input #2 :
        4
        1 2 5
        1 3 5
        1 4 5
    Output #2 :
        90
    Input #3 :
        5
        1 2 2
        2 3 3
        4 3 2
        5 3 2
    Output #3 :
        55
"""

import sys
sys.setrecursionlimit((2**31) - 1)

MOD = 1000000007

answer = 0


def treefy(parent, visited=set()):
    visited.add(parent)

    tree = {
        'weight': 0,
        'children': [],
    }
    for child, weight in edges[parent]:
        if child not in visited:
            subtree = treefy(child, visited)
            subtree['weight'] = weight
            tree['children'].append(subtree)

    return tree


def treeweight(tree):
    global answer

    children_weight = 1

    for child in tree['children']:
        child_weight = child['weight']
        subtree_weight = ((treeweight(child) * child_weight) % MOD)
        answer = ((answer + (subtree_weight * children_weight)) % MOD)
        children_weight = ((children_weight + subtree_weight) % MOD)

    return children_weight


n = int(input())

edges = {}
for i in range(1, n + 1):
    edges[i] = []
for i in range(1, n):
    a, b, w = map(int, input().split())
    edges[a].append((b, w))
    edges[b].append((a, w))

tree = treefy(1)
treeweight(tree)

print(answer)
