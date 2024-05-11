"""
    File: 124.py
    Title: Binary Tree Maximum Path Sum
    Difficulty: Hard
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.max = -987654321

        def maxPath(n):
            if n is None:
                return 0

            left = maxPath(n.left)
            right = maxPath(n.right)
            path = max(n.val, n.val + left, n.val + right)
            self.max = max(self.max, path, n.val + left + right)
            return path

        maxPath(root)

        return self.max
