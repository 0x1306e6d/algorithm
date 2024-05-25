"""
    File: 289.py
    Title: Game of Life
    Difficulty: Medium
"""

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]
        m = len(board)
        n = len(board[0])
        for y1 in range(m):
            for x1 in range(n):
                live = dead = 0
                for dx, dy in directions:
                    x2, y2 = x1 + dx, y1 + dy
                    if 0 <= x2 < n and 0 <= y2 < m:
                        if board[y2][x2] % 2 == 0:
                            dead += 1
                        else:
                            live += 1
                if board[y1][x1] == 0:
                    if live == 3:
                        board[y1][x1] = 2
                else:
                    if live == 2 or live == 3:
                        board[y1][x1] = 1
                    else:
                        board[y1][x1] = 3

        for y1 in range(m):
            for x1 in range(n):
                if board[y1][x1] == 2:
                    board[y1][x1] = 1
                if board[y1][x1] == 3:
                    board[y1][x1] = 0
