"""
    File: 136.py
    Title: Single Number
    Difficulty: Easy
    URL: https://leetcode.com/problems/single-number/
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans = ans ^ n
        return ans
