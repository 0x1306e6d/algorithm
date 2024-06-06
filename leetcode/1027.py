"""
    File: 1027.py
    Title: Longest Arithmetic Subsequence
    Difficulty: Medium
"""

from collections import defaultdict
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                if (i, diff) in dp:
                    dp[(j, diff)] = 1 + dp[(i, diff)]
                else:
                    dp[(j, diff)] = 2
        return max(dp.values())
