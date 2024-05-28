"""
    File: 2218.py
    Title: Maximum Value of K Coins From Piles
    Difficulty: Hard
"""

from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        for pile in piles:
            for i in range(1, len(pile)):
                pile[i] += pile[i - 1]

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            pile = piles[i]
            for kk in range(k, -1, -1):
                dp[i][kk] = dp[i + 1][kk]
                for j in range(min(kk, len(pile))):
                    dp[i][kk] = max(dp[i][kk], pile[j] + dp[i + 1][kk - j - 1])

        ans = 0
        for i in range(n):
            ans = max(ans, dp[i][k])
        return ans
