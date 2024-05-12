"""
    File: 85.py
    Title: Maximal Rectangle
    Difficulty: Hard
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        ans = 0
        memo = [[0] * cols for _ in range(rows)]
        for y in range(rows):
            for x in range(cols):
                if matrix[y][x] == "0":
                    continue
                if x > 0:
                    memo[y][x] = memo[y][x - 1] + 1
                else:
                    memo[y][x] = 1

                width = memo[y][x]
                for yy in range(y, -1, -1):
                    width = min(width, memo[yy][x])
                    area = (y - yy + 1) * width
                    ans = max(ans, area)
        return ans
