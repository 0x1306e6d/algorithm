"""
    File: 73.py
    Title: Set Matrix Zeroes
    Difficulty: Medium
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        has_y_zero = has_x_zero = False
        for y in range(m):
            if matrix[y][0] == 0:
                has_y_zero = True
                break
        for x in range(n):
            if matrix[0][x] == 0:
                has_x_zero = True
                break

        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0

        for y in range(1, m):
            for x in range(1, n):
                if matrix[y][0] == 0 or matrix[0][x] == 0:
                    matrix[y][x] = 0

        if has_y_zero:
            for y in range(m):
                matrix[y][0] = 0
        if has_x_zero:
            for x in range(n):
                matrix[0][x] = 0
