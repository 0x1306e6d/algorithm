"""
    File: 1035.py
    Title: Uncrossed Lines
    Difficulty: Medium
"""

from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for idx1 in range(n - 1, -1, -1):
            for idx2 in range(m - 1, -1, -1):
                dp[idx1][idx2] = max(dp[idx1 + 1][idx2], dp[idx1][idx2 + 1])
                if nums1[idx1] == nums2[idx2]:
                    dp[idx1][idx2] = max(dp[idx1][idx2], 1 + dp[idx1 + 1][idx2 + 1])
        return dp[0][0]
