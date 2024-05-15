"""
    File: 101.py
    Title: Symmetric Tree
    Difficulty: Easy
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lq = deque()
        lq.append(root.left)

        rq = deque()
        rq.append(root.right)

        while lq and rq:
            ll, rl = len(lq), len(rq)
            if ll != rl:
                return False
            for _ in range(ll):
                l, r = lq.popleft(), rq.popleft()
                if l is not None and r is not None:
                    if l.val != r.val:
                        return False
                else:
                    if l != r:
                        return False

                if l is not None:
                    lq.append(l.left)
                    lq.append(l.right)

                if r is not None:
                    rq.append(r.right)
                    rq.append(r.left)
        return True
