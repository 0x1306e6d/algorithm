"""
    File: 1218.py
    Title: Longest Arithmetic Subsequence of Given Difference
    Difficulty: Medium
"""

from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [0] * len(arr)
        nums = {}
        for i in range(len(arr)):
            num = arr[i]
            before = num - difference
            if before in nums:
                dp[i] = 1 + dp[nums[before]]
            else:
                dp[i] = 1
            nums[num] = i
        return max(dp)
