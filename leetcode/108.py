"""
    File: 108.py
    Title: Convert Sorted Array to Binary Search Tree
    Difficulty: Easy
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums) // 2
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid + 1 :])
        return TreeNode(nums[mid], left, right)
