"""
    File: 236.py
    Title: Lowest Common Ancestor of a Binary Tree
    Difficulty: Medium
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        depth = []

        def dfs(n, d):
            depth.append((n, d))
            if n.left is not None:
                dfs(n.left, d + 1)
            depth.append((n, d))
            if n.right is not None:
                dfs(n.right, d + 1)
            depth.append((n, d))

        dfs(root, 0)

        i, j = 0, 0
        while depth[i][0].val != p.val or depth[j][0].val != q.val:
            if depth[i][0].val != p.val:
                i += 1
            if depth[j][0].val != q.val:
                j += 1

        if i > j:
            i, j = j, i
        minimum = (None, 987654321)
        for k in range(i, j + 1):
            if depth[k][1] < minimum[1]:
                minimum = depth[k]
        return minimum[0]
