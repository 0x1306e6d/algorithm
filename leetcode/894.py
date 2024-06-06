"""
    File: 894.py
    Title: All Possible Full Binary Trees
    Difficulty: Medium
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode()]
        if n == 3:
            return [TreeNode(left=TreeNode(), right=TreeNode())]
        ans = []
        for i in range(1, n, 2):
            lefts = self.allPossibleFBT(i)
            rights = self.allPossibleFBT(n - 1 - i)
            for left in lefts:
                for right in rights:
                    ans.append(TreeNode(left=left, right=right))
        return ans
