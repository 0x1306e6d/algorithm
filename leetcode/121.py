"""
    File: 121.py
    Title: Best Time to Buy and Sell Stock
    Difficulty: Easy
    URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

import unittest

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        max_price = 0
        max_profit = 0
        for price in reversed(prices):
            max_profit = max(max_profit, max_price - price)
            max_price = max(max_price, price)
        return max_profit


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        prices = [7, 1, 5, 3, 6, 4]
        # Output
        output = 5

        solution = Solution()
        self.assertEqual(solution.maxProfit(prices), output)

    def test_example2(self):
        # Input
        prices = [7, 6, 4, 3, 1]
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.maxProfit(prices), output)


if __name__ == "__main__":
    unittest.main()
