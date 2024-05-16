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

        first, second = -1, -1
        for i in range(k):
            dp[0][i] = costs[0][i]
            if dp[0][i] < dp[0][second]:
                second = i
            if dp[0][i] < dp[0][first]:
                first, second = i, first

        for i in range(1, n):
            new_first, new_second = -1, -1
            for j in range(k):
                dp[i][j] = costs[i][j] + dp[i - 1][first if first != j else second]
                if dp[i][j] < dp[i][new_second]:
                    new_second = j
                if dp[i][j] < dp[i][new_first]:
                    new_first, new_second = j, new_first
            first, second = new_first, new_second
        return min(dp[-1])
