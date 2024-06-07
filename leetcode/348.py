"""
    File: 348.py
    Title: Design Tic-Tac-Toe
    Difficulty: Medium
"""


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            if self.rows[row] is None or self.rows[row] < 0:
                self.rows[row] = None
            else:
                self.rows[row] += 1
                if self.rows[row] == self.n:
                    return 1
            if self.cols[col] is None or self.cols[col] < 0:
                self.cols[col] = None
            else:
                self.cols[col] += 1
                if self.cols[col] == self.n:
                    return 1
        else:
            if self.rows[row] is None or self.rows[row] > 0:
                self.rows[row] = None
            else:
                self.rows[row] -= 1
                if self.rows[row] == -self.n:
                    return 2
            if self.cols[col] is None or self.cols[col] > 0:
                self.cols[col] = None
            else:
                self.cols[col] -= 1
                if self.cols[col] == -self.n:
                    return 2
        if row == col:
            if self.diag1 is not None:
                if player == 1 and self.diag1 >= 0:
                    self.diag1 += 1
                    if self.diag1 == self.n:
                        return 1
                elif player == 2 and self.diag1 <= 0:
                    self.diag1 -= 1
                    if self.diag1 == -self.n:
                        return 2
                else:
                    self.diag1 = None
        if self.n - 1 - row == col:
            if self.diag2 is not None:
                if player == 1 and self.diag2 >= 0:
                    self.diag2 += 1
                    if self.diag2 == self.n:
                        return 1
                elif player == 2 and self.diag2 <= 0:
                    self.diag2 -= 1
                    if self.diag2 == -self.n:
                        return 2
                else:
                    self.diag2 = None
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
