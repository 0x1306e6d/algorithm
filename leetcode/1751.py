"""
    File: 1751.py
    Title: Maximum Number of Events That Can Be Attended II
    Difficulty: Hard
"""

from functools import cache
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()

        @cache
        def attend(i, n):
            if n == 0:
                return 0
            if i >= len(events):
                return 0

            ans = attend(i + 1, n)

            start, end, value = events[i]
            j = i + 1
            while j < len(events):
                if events[j][0] > end:
                    break
                j += 1
            ans = max(ans, value + attend(j, n - 1))
            return ans

        return attend(0, k)
