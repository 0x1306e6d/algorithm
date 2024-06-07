"""
    File: 298.py
    Title: Binary Tree Longest Consecutive Sequence
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
        self.ans = 0

        def find(node):
            ans = 1
            if node.left:
                left = find(node.left)
                if (node.val - node.left.val) == -1:
                    ans = 1 + left
            if node.right:
                right = find(node.right)
                if (node.val - node.right.val) == -1:
                    ans = max(ans, 1 + right)
            self.ans = max(self.ans, ans)
            return ans

        find(root)

        return self.ans
