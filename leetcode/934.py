"""
    File: 934.py
    Title: Shortest Bridge
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        island = []
        for y in range(n):
            done = False
            for x in range(n):
                if grid[y][x] != 1:
                    continue
                grid[y][x] = 2

                q = deque()
                q.append((x, y))
                while q:
                    x1, y1 = q.popleft()
                    island.append((x1, y1))

                    for dx, dy in directions:
                        x2, y2 = x1 + dx, y1 + dy
                        if 0 <= x2 < n and 0 <= y2 < n:
                            if grid[y2][x2] == 1:
                                grid[y2][x2] = 2
                                q.append((x2, y2))

                done = True
                break
            if done:
                break

        q = deque()
        visited = [[False] * n for _ in range(n)]
        for x, y in island:
            q.append((x, y, 0))
            visited[y][x] = True
        while q:
            x1, y1, path = q.popleft()

            for dx, dy in directions:
                x2, y2 = x1 + dx, y1 + dy
                if 0 <= x2 < n and 0 <= y2 < n:
                    if visited[y2][x2]:
                        continue
                    visited[y2][x2] = True
                    if grid[y2][x2] == 1:
                        return path
                    elif grid[y2][x2] == 0:
                        q.append((x2, y2, path + 1))
