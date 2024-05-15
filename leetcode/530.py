"""
    File: 530.py
    Title: Minimum Absolute Difference in BST
    Difficulty: Easy
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans = 1e9

        self.prev = None

        def bst(node):
            if node is None:
                return
            bst(node.left)
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev.val)
            self.prev = node
            bst(node.right)

        bst(root)

        return self.ans
