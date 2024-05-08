"""
    File: 322.py
    Title: Coin Change
    Difficulty: Medium
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None] * (amount + 1)

        def _coinChange(amt):
            if amt == 0:
                return 0
            if memo[amt] is not None:
                return memo[amt]
            count = 987654321
            for coin in coins:
                if amt >= coin:
                    count = min(count, _coinChange(amt - coin) + 1)
            memo[amt] = count
            return count

        count = _coinChange(amount)
        if count == 987654321:
            return -1
        return count
