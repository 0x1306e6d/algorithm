"""
    File: 474.py
    Title: Ones and Zeroes
    Difficulty: Medium
"""

from functools import cache
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count(s):
            zero = one = 0
            for c in s:
                if c == "0":
                    zero += 1
                if c == "1":
                    one += 1
            return (zero, one)

        counts = list(map(count, strs))

        @cache
        def dp(i, z, o):
            if i == len(counts):
                return 0

            ans = dp(i + 1, z, o)
            zero, one = counts[i]
            if z >= zero and o >= one:
                ans = max(ans, 1 + dp(i + 1, z - zero, o - one))
            return ans

        return dp(0, m, n)
