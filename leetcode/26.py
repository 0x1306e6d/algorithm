"""
    File: 26.py
    Title: Remove Duplicates from Sorted Array
    Difficulty: Easy
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
            nums[i] = nums[j]
        return i + 1
