"""
    File: 105.py
    Title: Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = preorder[0]
        for i, n in enumerate(inorder):
            if n == root:
                break
        left = self.buildTree(preorder[1 : 1 + i], inorder[:i])
        right = self.buildTree(preorder[1 + i :], inorder[i + 1 :])
        return TreeNode(root, left, right)
