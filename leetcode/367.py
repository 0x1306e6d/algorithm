"""
    File: 367.py
    Title: Valid Perfect Square
    Difficulty: Easy
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo * lo <= num:
            mid = (lo + hi) // 2
            square = mid * mid
            if square == num:
                return True
            if square < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
