"""
    File: 75.py
    Title: Sort Colors
    Difficulty: Medium
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = white = blue = 0
        for n in nums:
            if n == 0:
                red += 1
            if n == 1:
                white += 1
            if n == 2:
                blue += 1
        for i in range(red):
            nums[i] = 0
        for i in range(red, red + white):
            nums[i] = 1
        for i in range(red + white, red + white + blue):
            nums[i] = 2
