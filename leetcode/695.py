"""
    File: 695.py
    Title: Max Area of Island
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ans = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 0:
                    continue
                grid[y][x] = 0

                area = 0
                q = deque()
                q.append((x, y))
                while q:
                    x1, y1 = q.popleft()
                    area += 1

                    for dx, dy in directions:
                        x2, y2 = x1 + dx, y1 + dy
                        if 0 <= x2 < n and 0 <= y2 < m:
                            if grid[y2][x2] == 1:
                                grid[y2][x2] = 0
                                q.append((x2, y2))
                ans = max(ans, area)
        return ans
