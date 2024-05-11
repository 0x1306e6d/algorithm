"""
    File: 329.py
    Title: Longest Increasing Path in a Matrix
    Difficulty: Hard
"""

from typing import List

__dx__ = [0, 0, -1, 1]
__dy__ = [-1, 1, 0, 0]


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        def _solution(x, y):
            if memo[y][x] > 0:
                return memo[y][x]

            longest = 0
            for dx, dy in zip(__dx__, __dy__):
                xx, yy = x + dx, y + dy
                if 0 <= xx < n and 0 <= yy < m:
                    if matrix[yy][xx] > matrix[y][x]:
                        longest = max(longest, _solution(xx, yy))
            longest += 1
            memo[y][x] = longest
            return longest

        ans = 0
        for y in range(m):
            for x in range(n):
                ans = max(ans, _solution(x, y))
        return ans
