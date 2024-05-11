"""
    File: 11.py
    Title: Container With Most Water
    Difficulty: Medium
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maximum = 0
        while i < j:
            water = (j - i) * min(height[j], height[i])
            maximum = max(maximum, water)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maximum
