"""
    File: 276.py
    Title: Paint Fence
    Difficulty: Medium
"""

from functools import lru_cache


class Solution:
    def numWays(self, n: int, k: int) -> int:
        @lru_cache
        def dp(i, c1, l):
            if i == n:
                return k - 1 if l == 2 else k

            ans = 0
            for c2 in range(k):
                if c1 == c2:
                    if l == 2:
                        continue
                    else:
                        ans += dp(i + 1, c1, l + 1)
                else:
                    ans += dp(i + 1, c2, 1)
            return ans

        return dp(1, -1, 0)
