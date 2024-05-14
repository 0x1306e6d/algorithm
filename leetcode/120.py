"""
    File: 120.py
    Title: Triangle
    Difficulty: Medium
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        dp = [[9876543210] * n for _ in range(n)]
        for i in range(n):
            dp[-1][i] = triangle[-1][i]
        for y1 in range(n - 2, -1, -1):
            for x1 in range(y1 + 1):
                for dx, dy in [(0, 1), (1, 1)]:
                    x2, y2 = x1 + dx, y1 + dy
                    if x2 <= y1 + 1:
                        dp[y1][x1] = min(dp[y1][x1], triangle[y1][x1] + dp[y2][x2])
        return dp[0][0]
