"""
    File: 270.py
    Title: Closest Binary Search Tree Value
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
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans, diff = root.val, abs(root.val - target)
        node = root
        while node:
            d = abs(node.val - target)
            if d < diff:
                ans = node.val
                diff = d
            elif d == diff:
                ans = min(ans, node.val)

            if target == node.val:
                break
            if target < node.val:
                node = node.left
            else:
                node = node.right
        return ans
