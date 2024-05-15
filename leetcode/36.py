"""
    File: 36.py
    Title: Valid Sudoku
    Difficulty: Medium
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(9):
            s = set()
            for x in range(9):
                c = board[y][x]
                if c != ".":
                    if c in s:
                        return False
                    s.add(c)
        for x in range(9):
            s = set()
            for y in range(9):
                c = board[y][x]
                if c != ".":
                    if c in s:
                        return False
                    s.add(c)
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                s = set()
                for y1 in range(y, y + 3):
                    for x1 in range(x, x + 3):
                        c = board[y1][x1]
                        if c != ".":
                            if c in s:
                                return False
                            s.add(c)
        return True
