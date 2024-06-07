"""
    File: 1254.py
    Title: Number of Closed Islands
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        ans = 0
        visited = [[False] * n for _ in range(n)]
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    continue
                if visited[y][x]:
                    continue
                visited[y][x] = True

                out = False
                q = deque()
                q.append((x, y))
                while q:
                    x1, y1 = q.popleft()
                    if x1 == 0 or x1 == (n - 1) or y1 == 0 or y1 == (m - 1):
                        out = True
                    for dx, dy in directions:
                        x2, y2 = x1 + dx, y1 + dy
                        if 0 <= x2 < n and 0 <= y2 < m:
                            if grid[y2][x2] == 0 and not visited[y2][x2]:
                                visited[y2][x2] = True
                                q.append((x2, y2))

                if not out:
                    ans += 1

        return ans
