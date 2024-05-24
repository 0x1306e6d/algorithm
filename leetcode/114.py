"""
    File: 114.py
    Title: Flatten Binary Tree to Linked List
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        def traverse(node):
            if node.right:
                traverse(node.right)

            left = node.left
            node.left = None
            if left:
                _, leftmost = traverse(left)
                if node.right:
                    right = node.right
                    node.right = left
                    leftmost.right = right
                else:
                    node.right = left

            rightmost = node
            while rightmost.right:
                rightmost = rightmost.right
            return node, rightmost

        traverse(root)
