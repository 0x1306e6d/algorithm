"""
    File: 1351.py
    Title: Count Negative Numbers in a Sorted Matrix
    Difficulty: Easy
"""

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        zero = 0
        for i in range(m):
            j = n - 1 - zero
            while j >= 0 and grid[i][j] < 0:
                zero += 1
                j -= 1
            ans += zero
        return ans
