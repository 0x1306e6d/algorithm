"""
    File: 1020.py
    Title: Number of Enclaves
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])
        ans = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 0:
                    continue

                q = deque()
                q.append((x, y))
                grid[y][x] = 0
                size = 0
                off = False
                while q:
                    x1, y1 = q.popleft()
                    size += 1
                    if x1 == 0 or x1 == n - 1 or y1 == 0 or y1 == m - 1:
                        off = True
                    for dx, dy in directions:
                        x2, y2 = x1 + dx, y1 + dy
                        if 0 <= x2 < n and 0 <= y2 < m:
                            if grid[y2][x2] == 1:
                                grid[y2][x2] = 0
                                q.append((x2, y2))
                if not off:
                    ans += size
        return ans
