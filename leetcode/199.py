"""
    File: 199.py
    Title: Binary Tree Right Side View
    Difficulty: Medium
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        q = deque()
        q.append(root)
        while q:
            qq = deque()
            while q:
                n = q.popleft()
                if n.left is not None:
                    qq.append(n.left)
                if n.right is not None:
                    qq.append(n.right)
            q = qq
            ans.append(n.val)
        return ans
