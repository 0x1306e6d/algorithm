"""
    File: 137.py
    Title: Single Number II
    Difficulty: Medium
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for shift in range(32):
            bit_sum = 0
            for n in nums:
                bit = (n >> shift) & 1
                bit_sum += bit
            bit = bit_sum % 3
            ans = ans | (bit << shift)
        if ans >= (1 << 31):
            ans = ans - (1 << 32)
        return ans
