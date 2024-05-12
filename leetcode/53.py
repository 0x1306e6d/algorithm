"""
    File: 53.py
    Title: Maximum Subarray
    Difficulty: Medium
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        memo = nums[0]
        for i in range(1, len(nums)):
            memo = max(memo + nums[i], nums[i])
            ans = max(ans, memo)
        return ans
