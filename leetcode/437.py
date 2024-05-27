"""
    File: 437.py
    Title: Path Sum III
    Difficulty: Medium
"""

from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        self.ans = 0
        self.prefix_sum = defaultdict(int)

        def dfs(node, path_sum):
            path_sum += node.val
            if path_sum == targetSum:
                self.ans += 1
            self.ans += self.prefix_sum[path_sum - targetSum]

            self.prefix_sum[path_sum] += 1
            if node.left:
                dfs(node.left, path_sum)
            if node.right:
                dfs(node.right, path_sum)
            self.prefix_sum[path_sum] -= 1

        dfs(root, 0)

        return self.ans
