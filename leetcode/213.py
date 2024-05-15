"""
    File: 213.py
    Title: House Robber II
    Difficulty: Medium
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        p1, p2 = 0, nums[1]
        for i in range(2, len(nums)):
            p1, p2 = max(p1, p2), max(p1 + nums[i], p2)
        ans = max(p1, p2)

        p1, p2 = nums[0], nums[1]
        for i in range(2, len(nums) - 1):
            p1, p2 = max(p1, p2), max(p1 + nums[i], p2)
        ans = max(ans, p1, p2)
        return ans
