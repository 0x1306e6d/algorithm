"""
    File: 790.py
    Title: Domino and Tromino Tiling
    Difficulty: Medium
"""

from functools import cache


mod = 10**9 + 7


class Solution:
    @cache
    def numTilings(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        ans = self.numTilings(n - 1)
        ans = (ans + self.numTilings(n - 2)) % mod
        for i in range(n):
            j = 3 + 2 * i
            if j <= n:
                ans = (ans + 2 * self.numTilings(n - j)) % mod
            else:
                break
        for i in range(n):
            j = 4 + 2 * i
            if j <= n:
                ans = (ans + 2 * self.numTilings(n - j)) % mod
            else:
                break
        return ans
