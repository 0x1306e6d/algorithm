"""
    File: 95.py
    Title: Unique Binary Search Trees II
    Difficulty: Medium
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[] for _ in range(n + 1)]
        dp[1] = [TreeNode()]
        for i in range(2, n + 1):
            for j in range(i):
                lefts = dp[j]
                rights = dp[i - j - 1]
                if lefts and rights:
                    for left in lefts:
                        for right in rights:
                            dp[i].append(TreeNode(left=left, right=right))
                elif lefts:
                    for left in lefts:
                        dp[i].append(TreeNode(left=left))
                else:
                    for right in rights:
                        dp[i].append(TreeNode(right=right))

        def copy(node, idx):
            if node is None:
                return idx, None
            idx, left = copy(node.left, idx)
            rightmost, right = copy(node.right, idx + 1)
            return rightmost, TreeNode(val=idx, left=left, right=right)

        ans = []
        for tree in dp[n]:
            _, root = copy(tree, 1)
            ans.append(root)
        return ans
