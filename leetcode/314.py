"""
    File: 314.py
    Title: Binary Tree Vertical Order Traversal
    Difficulty: Medium
"""

from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        memo = defaultdict(list)

        q = deque()
        q.append((root, 0))
        while q:
            qq = deque()
            while q:
                n, c = q.popleft()
                memo[c].append(n.val)

                if n.left is not None:
                    qq.append((n.left, c - 1))
                if n.right is not None:
                    qq.append((n.right, c + 1))
            q = qq

        ans = []
        for k in sorted(memo):
            ans.append(memo[k])
        return ans
