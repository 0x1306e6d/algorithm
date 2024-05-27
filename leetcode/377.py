"""
    File: 377.py
    Title: Combination Sum IV
    Difficulty: Medium
"""

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        inf = 1001
        dp = [0] * inf
        nums = list(sorted(nums))
        for n in nums:
            dp[n] = 1
        for i in range(1, target + 1):
            for n in nums:
                if i >= n:
                    dp[i] += dp[i - n]
                else:
                    break
        return dp[target]
