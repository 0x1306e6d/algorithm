"""
    File: 1230.py
    Title: Toss Strange Coins
    Difficulty: Medium
"""

from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1 - prob[0]
        dp[0][1] = prob[0]
        for i in range(1, n):
            p = prob[i]
            dp[i][0] = dp[i - 1][0] * (1 - p)
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j - 1] * p + dp[i - 1][j] * (1 - p)
            dp[i][i + 1] = dp[i - 1][i] * p
        return dp[n - 1][target]
