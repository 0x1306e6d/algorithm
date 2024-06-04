"""
    File: 268.py
    Title: Missing Number
    Difficulty: Easy
    URL: https://leetcode.com/problems/missing-number/
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans
