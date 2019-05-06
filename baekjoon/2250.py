"""
    2250 : 트리의 높이와 너비
    URL : https://www.acmicpc.net/problem/2250
    Input :
        19
        1 2 3
        2 4 5
        3 6 7
        4 8 -1
        5 9 10
        6 11 12
        7 13 -1
        8 -1 -1
        9 14 15
        10 -1 -1
        11 16 -1
        12 -1 -1
        13 17 -1
        14 -1 -1
        15 18 -1
        16 -1 -1
        17 -1 19
        18 -1 -1
        19 -1 -1
    Output :
        3 18
"""

tree = {}
tree2 = {}


def put(root=1, depth=1, width=0):
    ndescendants = 1

    left = tree[root]['left']
    if left is not None:
        ndescendants += put(left, depth + 1, width)
    width += ndescendants

    global tree2
    if depth not in tree2:
        tree2[depth] = []
    tree2[depth].append(width)

    right = tree[root]['right']
    if right is not None:
        ndescendants += put(right, depth + 1, width)

    return ndescendants


n = int(input())
root = set(range(1, n + 1))
for nn in range(1, n + 1):
    i, left, right = map(int, input().split())
    tree[i] = {
        'left': left if left != -1 else None,
        'right': right if right != -1 else None,
    }

    if left != -1:
        root.remove(left)
    if right != -1:
        root.remove(right)

root = root.pop()
put(root)

mdepth = 0
mwidth = 0
for depth in sorted(tree2):
    width = 1
    if len(tree2[depth]) >= 2:
        width = max(tree2[depth]) - min(tree2[depth]) + 1
    if width > mwidth:
        mdepth = depth
        mwidth = width


print("{} {}".format(mdepth, mwidth))
