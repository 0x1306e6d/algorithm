"""
    File: 877.py
    Title: Stone Game
    Difficulty: Medium
"""

from functools import cache
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(i, j, diff):
            if i > j:
                return True if diff > 0 else False
            if dp(i + 2, j, diff + piles[i] - piles[i + 1]):
                return True
            if dp(i + 1, j - 1, diff + piles[i] - piles[j]):
                return True
            if dp(i + 1, j - 1, diff + piles[j] - piles[i]):
                return True
            if dp(i, j - 2, diff + piles[j] - piles[j - 1]):
                return True
            return False

        return dp(0, len(piles) - 1, 0)
