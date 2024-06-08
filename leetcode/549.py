"""
    File: 549.py
    Title: Binary Tree Longest Consecutive Sequence II
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
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            inc = dec = longest = 1
            left_inc = left_dec = left_longest = 0
            right_inc = right_dec = right_longest = 0
            if node.left:
                left_inc, left_dec, left_longest = dfs(node.left)
                if node.left.val + 1 == node.val:
                    dec = left_dec + 1
                if node.left.val - 1 == node.val:
                    inc = left_inc + 1
            if node.right:
                right_inc, right_dec, right_longest = dfs(node.right)
                if node.right.val + 1 == node.val:
                    dec = max(dec, right_dec + 1)
                if node.right.val - 1 == node.val:
                    inc = max(inc, right_inc + 1)
            if node.left and node.right:
                if node.left.val + 1 == node.val == node.right.val - 1:
                    longest = left_dec + 1 + right_inc
                if node.left.val - 1 == node.val == node.right.val + 1:
                    longest = max(longest, left_inc + 1 + right_dec)
            return inc, dec, max(longest, inc, dec, left_longest, right_longest)

        return dfs(root)[2]
