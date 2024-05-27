"""
    File: 875.py
    Title: Koko Eating Bananas
    Difficulty: Medium
"""

from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2

            hours = 0
            for pile in piles:
                hours += ceil(pile / mid)

            if hours > h:
                lo = mid + 1
            else:
                hi = mid
        return lo
