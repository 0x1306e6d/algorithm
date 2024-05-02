"""
    File: 623.py
    Title: Add One Row to Tree
    Difficulty: Medium
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        parents = [root]
        for d in range(depth - 2):
            new_parents = []
            for p in parents:
                if p.left is not None:
                    new_parents.append(p.left)
                if p.right is not None:
                    new_parents.append(p.right)
            parents = new_parents
        for p in parents:
            p.left = TreeNode(val, left=p.left)
            p.right = TreeNode(val, right=p.right)
        return root
