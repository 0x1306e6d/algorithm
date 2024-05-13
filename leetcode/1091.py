"""
    File: 1091.py
    Title: Populating Next Right Pointers in Each Node
    Difficulty: Medium
"""

from collections import deque
from typing import List

__dx__ = [-1, 0, 1, 1, 1, 0, -1, -1]
__dy__ = [-1, -1, -1, 0, 1, 1, 1, 0]


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)

        q = deque()
        q.append((0, 0, 1))
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        while q:
            x1, y1, p = q.popleft()
            if x1 == n - 1 and y1 == n - 1:
                return p
            for dx, dy in zip(__dx__, __dy__):
                x2, y2 = x1 + dx, y1 + dy
                if 0 <= x2 < n and 0 <= y2 < n:
                    if grid[y2][x2] == 1:
                        continue
                    if visited[y2][x2]:
                        continue
                    visited[y2][x2] = True
                    q.append((x2, y2, p + 1))
        return -1
