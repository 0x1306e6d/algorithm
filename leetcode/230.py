"""
    File: 230.py
    Title: Kth Smallest Element in a BST
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find(node, p):
            ans = None
            if node.left:
                ans, p = find(node.left, p)
                if ans is not None:
                    return ans, k
            p += 1
            if p == k:
                return node.val, k
            if node.right:
                ans, p = find(node.right, p)
            return ans, p

        ans, _ = find(root, 0)
        return ans
