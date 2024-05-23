"""
    File: 687.py
    Title: Longest Univalue Path
    Difficulty: Medium
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.ans = 0

        def dfs(node):
            if node is None:
                return

            node.left_length = 0
            node.right_length = 0

            dfs(node.left)
            dfs(node.right)

            if node.left is not None and node.val == node.left.val:
                node.left_length = 1 + max(
                    node.left.left_length,
                    node.left.right_length,
                )

            if node.right is not None and node.val == node.right.val:
                node.right_length = 1 + max(
                    node.right.left_length,
                    node.right.right_length,
                )

            self.ans = max(self.ans, node.left_length + node.right_length)

        dfs(root)

        return self.ans
