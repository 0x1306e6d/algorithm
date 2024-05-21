"""
    File: 2971.py
    Title: Find Polygon With the Largest Perimeter
    Difficulty: Medium
"""

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans = -1
        sides = None
        for n in sorted(nums):
            if sides is None:
                sides = n
                continue
            if sides > n:
                ans = sides + n
            sides += n
        return ans
