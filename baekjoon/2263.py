"""
    2263 : 트리의 순회
    URL : https://www.acmicpc.net/problem/2263
    Input :
        3
        1 2 3
        1 3 2
    Output :
        2 1 3
"""

import sys
sys.setrecursionlimit(987654321)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []


def dft(i_low, i_high, p_low, p_high):
    if (i_low <= i_high) and (p_low <= p_high):
        root = postorder[p_high]
        preorder.append(root)

        pivot = inorder.index(root)
        n_left = pivot - i_low
        n_right = i_high - pivot
        dft(i_low, i_low + n_left - 1, p_low, p_low + n_left - 1)
        dft(i_high - n_right + 1, i_high, p_high - n_right, p_high - 1)


dft(0, n - 1, 0, n - 1)
print("{}".format(' '.join(str(i) for i in preorder)))
