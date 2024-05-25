"""
    File: 701.py
    Title: Insert into a Binary Search Tree
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        node = root
        while node:
            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    break
            else:
                if node.left:
                    node = node.left
                else:
                    break

        if val > node.val:
            node.right = TreeNode(val)
        else:
            node.left = TreeNode(val)

        return root
