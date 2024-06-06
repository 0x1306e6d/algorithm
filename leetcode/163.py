"""
    File: 163.py
    Title: Missing Ranges
    Difficulty: Easy
"""

from typing import List


class Solution:
    def findMissingRanges(
        self,
        nums: List[int],
        lower: int,
        upper: int,
    ) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]

        ans = []
        if lower < nums[0]:
            ans.append([lower, nums[0] - 1])
        for i in range(1, len(nums)):
            current, prev = nums[i], nums[i - 1]
            if current - prev == 1:
                pass
            else:
                ans.append([prev + 1, current - 1])
        if upper > nums[-1]:
            ans.append([nums[-1] + 1, upper])
        return ans
