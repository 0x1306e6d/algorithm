"""
    File: 172.py
    Title: Factorial Trailing Zeroes
    Difficulty: Medium
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            m = i
            while m % 5 == 0:
                ans += 1
                m //= 5
        return ans
