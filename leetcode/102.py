"""
    File: 102.py
    Title: Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        q = deque()
        q.append(root)
        while q:
            qq = deque()
            level = []
            while q:
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    qq.append(node.left)
                if node.right:
                    qq.append(node.right)
            ans.append(level)
            q = qq
        return ans
