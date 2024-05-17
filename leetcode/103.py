"""
    File: 103.py
    Title: Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        q = deque()
        q.append(root)
        i = 1
        while q:
            qq = deque()
            level = []
            while q:
                n = q.popleft()
                level.append(n.val)

                if n.left is not None:
                    qq.append(n.left)
                if n.right is not None:
                    qq.append(n.right)
            if i % 2 == 0:
                ans.append(list(reversed(level)))
            else:
                ans.append(level)
            q = qq
            i += 1
        return ans
