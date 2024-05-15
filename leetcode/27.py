"""
    File: 27.py
    Title: Remove Element
    Difficulty: Easy
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, len(nums)
        while i < k:
            if nums[i] == val:
                j = k - 1
                nums[i], nums[j] = nums[j], nums[i]
                k -= 1
            else:
                i += 1
        return k
