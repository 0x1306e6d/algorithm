"""
    File: 1539.py
    Title: Kth Missing Positive Number
    Difficulty: Easy
"""

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            missing = arr[mid] - mid - 1
            if missing < k:
                lo = mid + 1
            else:
                hi = mid
        if lo == 0:
            return k
        return arr[lo - 1] + (k - arr[lo - 1] + lo)
