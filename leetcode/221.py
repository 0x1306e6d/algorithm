"""
    File: 221.py
    Title: Maximal Square
    Difficulty: Medium
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        memo = [[0] * (n + 1) for _ in range(m + 1)]
        side = 0
        for y in range(1, m + 1):
            for x in range(1, n + 1):
                if matrix[y - 1][x - 1] == "0":
                    continue
                memo[y][x] = min(memo[y - 1][x - 1], memo[y - 1][x], memo[y][x - 1]) + 1
                side = max(side, memo[y][x])
        return side * side
