"""
    File: 714.py
    Title: Best Time to Buy and Sell Stock with Transaction Fee
    Difficulty: Medium
    URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""

import unittest

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -prices[0]
        sell = 0
        for i in range(1, len(prices)):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        return sell


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        prices = [1, 3, 2, 8, 4, 9]
        fee = 2
        # Output
        output = 8

        solution = Solution()
        self.assertEqual(solution.maxProfit(prices, fee), output)

    def test_example2(self):
        # Input
        prices = [1, 3, 7, 5, 10, 3]
        fee = 3
        # Output
        output = 6

        solution = Solution()
        self.assertEqual(solution.maxProfit(prices, fee), output)


if __name__ == "__main__":
    unittest.main()
