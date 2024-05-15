"""
    File: 637.py
    Title: Average of Levels in Binary Tree
    Difficulty: Easy
"""

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque()
        q.append(root)
        while q:
            d = len(q)
            values, count = 0, 0
            for _ in range(d):
                n = q.popleft()
                values += n.val
                count += 1

                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
            ans.append(values / count)
        return ans
