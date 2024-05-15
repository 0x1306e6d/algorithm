"""
    File: 188.py
    Title: Best Time to Buy and Sell Stock IV
    Difficulty: Hard
"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {}

        def dp(i, kk, h):
            if kk == 0:
                return 0
            if i >= len(prices):
                return 0
            if (i, kk, h) in memo:
                return memo[(i, kk, h)]

            ans = 0
            if h:
                ans = max(ans, prices[i] + dp(i + 1, kk - 1, False))
                ans = max(ans, dp(i + 1, kk, True))
            else:
                ans = max(ans, -prices[i] + dp(i + 1, kk, True))
                ans = max(ans, dp(i + 1, kk, False))
            memo[(i, kk, h)] = ans
            return ans

        return dp(0, k, False)
