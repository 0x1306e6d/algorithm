"""
    File: 80.py
    Title: Remove Duplicates from Sorted Array II
    Difficulty: Medium
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        value, count = nums[0], 0
        while j < len(nums):
            nums[i] = nums[j]
            if value == nums[j]:
                count += 1
            else:
                value = nums[j]
                count = 1
            if count <= 2:
                i += 1
            j += 1
        return i
