"""
    File: 429.py
    Title: N-ary Tree Level Order Traversal
    Difficulty: Medium
"""

from collections import deque
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if root is None:
            return []

        ans = []

        q = deque()
        q.append(root)
        while q:
            qq = deque()
            level = []
            while q:
                p = q.popleft()
                level.append(p.val)

                for c in p.children:
                    qq.append(c)
            q = qq
            ans.append(level)

        return ans
