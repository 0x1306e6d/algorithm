"""
    File: 931.py
    Title: Minimum Falling Path Sum
    Difficulty: Medium
"""

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        inf = float("inf")
        n = len(matrix)
        dp = [[inf] * n for _ in range(n)]
        for x in range(n):
            dp[0][x] = matrix[0][x]
        for y in range(1, n):
            for x in range(n):
                m = matrix[y][x]
                dp[y][x] = dp[y - 1][x] + m
                if x > 0:
                    dp[y][x] = min(dp[y][x], dp[y - 1][x - 1] + m)
                if x < n - 1:
                    dp[y][x] = min(dp[y][x], dp[y - 1][x + 1] + m)
        return min(dp[-1])
