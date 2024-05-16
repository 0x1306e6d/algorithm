"""
    File: 265.py
    Title: Paint House II
    Difficulty: Hard
"""

from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        inf = float("inf")
        n, k = len(costs), len(costs[0])
        dp = [[inf] * k for _ in range(n)]
        for i in range(k):
            dp[0][i] = costs[0][i]
        for i in range(1, n):
            for j1 in range(k):
                cost = inf
                for j2 in range(k):
                    if j1 == j2:
                        continue
                    cost = min(cost, dp[i - 1][j2])
                dp[i][j1] = costs[i][j1] + cost
        return min(dp[-1])
