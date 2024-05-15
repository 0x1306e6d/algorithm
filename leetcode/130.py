"""
    File: 130.py
    Title: Surrounded Regions
    Difficulty: Medium
"""

from collections import deque
from typing import List

__d__ = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def bfs(x, y):
            board[y][x] = "N"

            q = deque()
            q.append((x, y))
            while q:
                x1, y1 = q.popleft()
                for dx, dy in __d__:
                    x2, y2 = x1 + dx, y1 + dy
                    if 0 <= x2 < n and 0 <= y2 < m:
                        if board[y2][x2] == "O":
                            board[y2][x2] = "N"
                            q.append((x2, y2))

        for x1 in range(n):
            if board[0][x1] == "O":
                bfs(x1, 0)
            if board[m - 1][x1] == "O":
                bfs(x1, m - 1)
        for y1 in range(m):
            if board[y1][0] == "O":
                bfs(0, y1)
            if board[y1][n - 1] == "O":
                bfs(n - 1, y1)

        for y in range(m):
            for x in range(n):
                if board[y][x] == "O":
                    board[y][x] = "X"
                elif board[y][x] == "N":
                    board[y][x] = "O"
