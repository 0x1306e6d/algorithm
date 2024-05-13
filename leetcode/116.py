"""
    File: 116.py
    Title: Populating Next Right Pointers in Each Node
    Difficulty: Medium
"""

from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None:
            return None

        q = deque()
        q.append(root)
        while q:
            prev = None
            qq = deque()
            while q:
                n = q.popleft()
                if prev is None:
                    prev = n
                else:
                    prev.next = n
                    prev = n
                if n.left is not None:
                    qq.append(n.left)
                if n.right is not None:
                    qq.append(n.right)
            q = qq
        return root
