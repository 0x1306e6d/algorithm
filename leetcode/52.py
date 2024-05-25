"""
    File: 52.py
    Title: N-Queens II
    Difficulty: Hard
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cols = [False] * n
        self.diag1 = [False] * (2 * n - 1)
        self.diag2 = [False] * (2 * n - 1)

        def nqueen(y):
            if y == n:
                return 1
            ans = 0
            for x in range(n):
                d1 = y + x
                d2 = (n - y - 1) + x
                if self.cols[x] or self.diag1[d1] or self.diag2[d2]:
                    continue
                self.cols[x] = self.diag1[d1] = self.diag2[d2] = True
                ans += nqueen(y + 1)
                self.cols[x] = self.diag1[d1] = self.diag2[d2] = False
            return ans

        return nqueen(0)
