"""
    1991 : 트리 순회
    URL : https://www.acmicpc.net/problem/1991
    Input :
        7
        A B C
        B D .
        C E F
        E . .
        F . G
        D . .
        G . .
    Output :
        ABDCEFG
        DBAECFG
        DBEGFCA
"""

tree = {}


def preorder(root):
    traversal = []
    traversal += root
    if tree[root]['left'] is not None:
        traversal += preorder(tree[root]['left'])
    if tree[root]['right'] is not None:
        traversal += preorder(tree[root]['right'])
    return traversal


def inorder(root):
    traversal = []
    if tree[root]['left'] is not None:
        traversal += inorder(tree[root]['left'])
    traversal += root
    if tree[root]['right'] is not None:
        traversal += inorder(tree[root]['right'])
    return traversal


def postorder(root):
    traversal = []
    if tree[root]['left'] is not None:
        traversal += postorder(tree[root]['left'])
    if tree[root]['right'] is not None:
        traversal += postorder(tree[root]['right'])
    traversal += root
    return traversal


n = int(input())
for i in range(n):
    name, left, right = input().split()
    tree[name] = {
        'left': left if left is not '.' else None,
        'right': right if right is not '.' else None,
    }

print(''.join(preorder('A')))
print(''.join(inorder('A')))
print(''.join(postorder('A')))
