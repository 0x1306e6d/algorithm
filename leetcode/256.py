"""
    File: 256.py
    Title: Paint House
    Difficulty: Medium
"""

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        inf = float("inf")
        n = len(costs)
        dp = [[inf, inf, inf] for _ in range(n)]
        dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2]
        for i in range(1, n):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
        return min(dp[-1])
