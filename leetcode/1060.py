"""
    File: 1060.py
    Title: Missing Element in Sorted Array
    Difficulty: Medium
"""

from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] - nums[0] - mid < k:
                lo = mid + 1
            else:
                hi = mid
        return nums[0] + k + lo - 1
