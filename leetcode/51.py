"""
    File: 51.py
    Title: N-Queens
    Difficulty: Hard
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.cols = [False] * n
        self.diag1 = [False] * (2 * n - 1)
        self.diag2 = [False] * (2 * n - 1)

        self.ans = []

        def nqueen(y, queens):
            if y == n:
                board = [["."] * n for _ in range(n)]
                for x, y in queens:
                    board[y][x] = "Q"
                board = list(map(lambda row: "".join(row), board))
                self.ans.append(board)
                return
            for x in range(n):
                d1 = y + x
                d2 = n - y - 1 + x
                if self.cols[x] or self.diag1[d1] or self.diag2[d2]:
                    continue
                self.cols[x] = self.diag1[d1] = self.diag2[d2] = True
                queens.append((x, y))
                nqueen(y + 1, queens)
                queens.pop()
                self.cols[x] = self.diag1[d1] = self.diag2[d2] = False

        nqueen(0, [])

        return self.ans
