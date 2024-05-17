"""
    File: 983.py
    Title: Minimum Cost For Tickets
    Difficulty: Medium
"""

from functools import lru_cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def find(x):
            i, j = 0, len(days)
            while i < j:
                mid = (i + j) // 2
                if days[mid] < x:
                    i = mid + 1
                else:
                    j = mid
            return i

        @lru_cache
        def dp(i):
            if i >= len(days):
                return 0
            return min(
                costs[0] + dp(i + 1),
                costs[1] + dp(find(days[i] + 7)),
                costs[2] + dp(find(days[i] + 30)),
            )

        return dp(0)
