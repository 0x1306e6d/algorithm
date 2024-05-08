"""
    File: 518.py
    Title: Coin Change II
    Difficulty: Medium
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [0] * (amount + 1)
        memo[0] = 1
        for coin in sorted(coins):
            for i in range(amount + 1):
                if i - coin >= 0:
                    memo[i] += memo[i - coin]
        return memo[amount]
