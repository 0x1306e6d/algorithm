"""
    File: 7.py
    Title: Reverse Integer
    Difficulty: Medium
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = x < 0
        x = abs(x)
        ans = 0
        while x > 0:
            ans *= 10
            ans += x % 10
            x //= 10
        if ans > 2147483647:
            return 0
        if sign:
            ans *= -1
        return ans
