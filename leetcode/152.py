"""
    File: 152.py
    Title: Maximum Product Subarray
    Difficulty: Medium
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        top = bottom = nums[0]
        ans = top
        for i in range(1, len(nums)):
            n = nums[i]
            next_top = max(n, top * n, bottom * n)
            bottom = min(n, top * n, bottom * n)
            top = next_top
            ans = max(ans, top)
        return ans
