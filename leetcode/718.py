"""
    File: 718.py
    Title: Maximum Length of Repeated Subarray
    Difficulty: Medium
"""

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i1 in range(1, n + 1):
            for i2 in range(1, m + 1):
                if nums1[i1 - 1] == nums2[i2 - 1]:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1
                    ans = max(ans, dp[i1][i2])
        return ans
