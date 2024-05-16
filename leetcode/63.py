"""
    File: 63.py
    Title: Unique Paths II
    Difficulty: Medium
    URL: https://leetcode.com/problems/unique-paths-ii/
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for y in range(m):
            for x in range(n):
                if obstacleGrid[y][x] == 1:
                    continue
                if y > 0:
                    dp[y][x] += dp[y - 1][x]
                if x > 0:
                    dp[y][x] += dp[y][x - 1]
        return dp[m - 1][n - 1]
