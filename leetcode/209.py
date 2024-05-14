"""
    File: 209.py
    Title: Minimum Size Subarray Sum
    Difficulty: Medium
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 987654321
        sub, j = 0, 0
        for i in range(len(nums)):
            if sub < target:
                sub += nums[i]
            while sub >= target:
                ans = min(ans, i - j + 1)
                sub -= nums[j]
                j += 1
        if ans == 987654321:
            return 0
        return ans
