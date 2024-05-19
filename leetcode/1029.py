"""
    File: 1029.py
    Title: Two City Scheduling
    Difficulty: Medium
"""

from functools import lru_cache
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2

        @lru_cache
        def dp(i, a):
            if i >= len(costs):
                return 0
            b = i - a
            if a == n:
                return costs[i][1] + dp(i + 1, a)
            if b == n:
                return costs[i][0] + dp(i + 1, a + 1)
            return min(costs[i][1] + dp(i + 1, a), costs[i][0] + dp(i + 1, a + 1))

        return dp(0, 0)
