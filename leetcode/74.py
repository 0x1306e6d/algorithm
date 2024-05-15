"""
    File: 74.py
    Title: Search a 2D Matrix
    Difficulty: Medium
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m * n - 1
        while i <= j:
            mid = (i + j) // 2
            x, y = mid % n, mid // n
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False
