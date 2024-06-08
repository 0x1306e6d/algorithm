"""
    File: 272.py
    Title: Closest Binary Search Tree Value II
    Difficulty: Hard
"""

from collections import deque
from heapq import heappop, heappush
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(
        self,
        root: Optional[TreeNode],
        target: float,
        k: int,
    ) -> List[int]:
        h = []

        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            heappush(h, (abs(node.val - target), node.val))

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        ans = []
        for i in range(k):
            diff, val = heappop(h)
            ans.append(val)
        return ans
