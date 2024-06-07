"""
    File: 490.py
    Title: The Maze
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def hasPath(
        self,
        maze: List[List[int]],
        start: List[int],
        destination: List[int],
    ) -> bool:
        m, n = len(maze), len(maze[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        src_y, src_x = start
        dst_y, dst_x = destination

        q = deque()
        q.append((src_x, src_y))
        visited = [[False] * n for _ in range(m)]
        visited[src_y][src_x] = True
        while q:
            x1, y1 = q.popleft()
            if x1 == dst_x and y1 == dst_y:
                return True

            for dx, dy in directions:
                x2, y2 = x1 + dx, y1 + dy
                while 0 <= x2 < n and 0 <= y2 < m and maze[y2][x2] == 0:
                    x2 += dx
                    y2 += dy
                x2 -= dx
                y2 -= dy
                if not visited[y2][x2]:
                    visited[y2][x2] = True
                    q.append((x2, y2))
        return False
