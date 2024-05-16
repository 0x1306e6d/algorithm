"""
    File: 714.py
    Title: Best Time to Buy and Sell Stock with Transaction Fee
    Difficulty: Medium
    URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""

from functools import lru_cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache
        def dp(i, h):
            if i >= len(prices):
                return 0
            if h:
                return max(-fee + prices[i] + dp(i + 1, False), dp(i + 1, True))
            else:
                return max(-prices[i] + dp(i + 1, True), dp(i + 1, False))

        return dp(0, False)
