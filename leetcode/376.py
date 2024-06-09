"""
    File: 376.py
    Title: Wiggle Subsequence
    Difficulty: Medium
"""

from functools import cache
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @cache
        def dp(i, inc):
            if i >= len(nums):
                return 1
            ans = dp(i + 1, inc)
            for j in range(i + 1, len(nums)):
                if inc and nums[j] > nums[i]:
                    ans = max(ans, 1 + dp(j, False))
                    break
                if not inc and nums[j] < nums[i]:
                    ans = max(ans, 1 + dp(j, True))
                    break
            return ans

        return max(dp(0, True), dp(0, False))
