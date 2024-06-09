"""
    File: 1463.py
    Title: Cherry Pickup II
    Difficulty: Hard
"""

from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        inf = float("inf")

        @cache
        def dp(r, c1, c2):
            if c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
                return -inf
            ans = grid[r][c1]
            if c1 != c2:
                ans += grid[r][c2]
            if r == m - 1:
                return ans
            add = 0
            for new_c1 in [c1 - 1, c1, c1 + 1]:
                for new_c2 in [c2 - 1, c2, c2 + 1]:
                    add = max(add, dp(r + 1, new_c1, new_c2))
            return ans + add

        return max(0, dp(0, 0, n - 1))
