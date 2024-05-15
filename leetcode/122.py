"""
    File: 122.py
    Title: Best Time to Buy and Sell Stock II
    Difficulty: Medium
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        maximum = prices[0]
        minimum = prices[0]
        for i in range(1, len(prices)):
            p = prices[i]
            if p > maximum:
                maximum = p
            else:
                ans += maximum - minimum
                maximum, minimum = p, p
        ans += maximum - minimum
        return ans
