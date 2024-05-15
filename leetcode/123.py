"""
    File: 123.py
    Title: Best Time to Buy and Sell Stock III
    Difficulty: Hard
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = [0] * n
        right = [0] * n
        buy = prices[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], prices[i] - buy)
            buy = min(buy, prices[i])
        sell = prices[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], sell - prices[i])
            sell = max(sell, prices[i])
        ans = 0
        for l, r in zip(left, right):
            ans = max(ans, l + r)
        return ans
