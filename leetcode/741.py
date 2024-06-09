"""
    File: 741.py
    Title: Cherry Pickup
    Difficulty: Hard
"""

from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = [[[None] * n for _ in range(n)] for _ in range(n)]
        inf = float("inf")

        @cache
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if r1 == n or c1 == n or r2 == n or c2 == n:
                return -inf
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -inf
            if r1 == c1 == n - 1:
                return grid[r1][c1]
            if memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]

            ans = grid[r1][c1]
            if r1 != r2 and c1 != c2:
                ans += grid[r2][c2]
            ans += max(
                dp(r1 + 1, c1, c2),
                dp(r1 + 1, c1, c2 + 1),
                dp(r1, c1 + 1, c2),
                dp(r1, c1 + 1, c2 + 1),
            )
            return ans

        return max(0, dp(0, 0, 0))
