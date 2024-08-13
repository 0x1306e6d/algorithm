"""
    File: 1161.py
    Title: Maximum Level Sum of a Binary Tree
    Difficulty: Medium
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = level = 1
        maximum_sum = -float("inf")
        q = deque()
        q.append(root)
        while q:
            s = 0
            q2 = deque()

            while q:
                node = q.popleft()
                s += node.val

                if node.left is not None:
                    q2.append(node.left)
                if node.right is not None:
                    q2.append(node.right)

            if s > maximum_sum:
                ans = level
                maximum_sum = s
            level += 1
            q = q2

        return ans
