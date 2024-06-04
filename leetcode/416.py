"""
    File: 416.py
    Title: Partition Equal Subset Sum
    Difficulty: Medium
"""

from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2

        @cache
        def backtrace(i, x):
            if x == target:
                return True
            if i == len(nums):
                return False
            return backtrace(i + 1, x) or backtrace(i + 1, x + nums[i])

        return backtrace(0, 0)
