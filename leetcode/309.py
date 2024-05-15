"""
    File: 309.py
    Title: Best Time to Buy and Sell Stock with Cooldown
    Difficulty: Medium
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[0, 0] for _ in range(len(prices) + 2)]

        for i in range(len(prices) - 1, -1, -1):
            memo[i][0] = max(memo[i + 1][0], -prices[i] + memo[i + 1][1])
            memo[i][1] = max(memo[i + 1][1], prices[i] + memo[i + 2][0])
        return memo[0][0]
