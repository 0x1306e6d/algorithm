"""
    File: 827.py
    Title: Making A Large Island
    Difficulty: Hard
"""

from collections import deque
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        max_island = 0
        island_id = 2
        islands = {}
        for y in range(n):
            for x in range(n):
                if grid[y][x] != 1:
                    continue

                size = 0
                grid[y][x] = island_id

                q = deque()
                q.append((x, y))
                while q:
                    x1, y1 = q.popleft()
                    size += 1
                    for dx, dy in directions:
                        x2, y2 = x1 + dx, y1 + dy
                        if 0 <= x2 < n and 0 <= y2 < n:
                            if grid[y2][x2] == 1:
                                grid[y2][x2] = island_id
                                q.append((x2, y2))
                max_island = max(max_island, size)
                islands[island_id] = size
                island_id += 1

        ans = 0
        for y1 in range(n):
            for x1 in range(n):
                if grid[y1][x1] != 0:
                    continue
                connected = set()
                for dx, dy in directions:
                    x2, y2 = x1 + dx, y1 + dy
                    if 0 <= x2 < n and 0 <= y2 < n:
                        if grid[y2][x2] != 0:
                            connected.add(grid[y2][x2])
                size = 1
                for i in connected:
                    size += islands[i]
                ans = max(ans, size)
        if ans == 0:
            return max_island
        return ans
