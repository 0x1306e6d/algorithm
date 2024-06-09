"""
    File: 250.py
    Title: Count Univalue Subtrees
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
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.ans = 0

        def traverse(node):
            univalue = True
            if node.left:
                left = traverse(node.left)
                if not left or node.val != node.left.val:
                    univalue = False
            if node.right:
                right = traverse(node.right)
                if not right or node.val != node.right.val:
                    univalue = False
            if univalue:
                self.ans += 1
            return univalue

        traverse(root)

        return self.ans
