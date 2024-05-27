"""
    File: 1926.py
    Title: Nearest Exit from Entrance in Maze
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        q = deque()
        q.append((entrance[1], entrance[0], 0))
        visited = [[False] * n for _ in range(m)]
        visited[entrance[0]][entrance[1]] = True
        while q:
            x1, y1, count = q.popleft()
            for dx, dy in directions:
                x2, y2 = x1 + dx, y1 + dy
                if 0 <= x2 < n and 0 <= y2 < m:
                    if maze[y2][x2] == "+":
                        continue
                    if visited[y2][x2]:
                        continue
                    visited[y2][x2] = True
                    if x2 == 0 or x2 == n - 1 or y2 == 0 or y2 == m - 1:
                        return count + 1
                    q.append((x2, y2, count + 1))
        return -1
