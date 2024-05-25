"""
    File: 190.py
    Title: Reverse Bits
    Difficulty: Easy
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31, -1, -1):
            ans = ans | ((n & 1) << i)
            n = n >> 1
        return ans
