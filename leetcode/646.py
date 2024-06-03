"""
    File: 646.py
    Title: Maximum Length of Pair Chain
    Difficulty: Medium
"""

from functools import cache
from typing import List


def bisect_right(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid][0] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()

        @cache
        def dp(i):
            if i >= len(pairs):
                return 0

            ans = dp(i + 1)

            j = bisect_right(pairs, pairs[i][1])
            ans = max(ans, 1 + dp(j))
            return ans

        return dp(0)
