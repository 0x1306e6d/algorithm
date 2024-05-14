"""
    File: 994.py
    Title: Rotting Oranges
    Difficulty: Medium
"""

from collections import deque
from typing import List

__dx__ = [0, 0, -1, 1]
__dy__ = [-1, 1, 0, 0]
__inf__ = 9876543210


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        minutes = [[0] * n for _ in range(m)]

        q = deque()
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    minutes[y][x] = __inf__
                elif grid[y][x] == 2:
                    q.append((x, y))

        while q:
            x1, y1 = q.popleft()
            for dx, dy in zip(__dx__, __dy__):
                x2, y2 = x1 + dx, y1 + dy
                if 0 <= x2 < n and 0 <= y2 < m:
                    if grid[y2][x2] != 1:
                        continue
                    minute = minutes[y1][x1] + 1
                    if minutes[y2][x2] > minute:
                        minutes[y2][x2] = minute
                        q.append((x2, y2))

        ans = 0
        for m in minutes:
            ans = max(ans, max(m))
        if ans == __inf__:
            ans = -1
        return ans
