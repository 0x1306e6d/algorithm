"""
    File: 688.py
    Title: Knight Probability in Chessboard
    Difficulty: Medium
"""


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
        ]

        memo = [[0] * n for _ in range(n)]
        memo[row][column] = 1
        for _ in range(k):
            new_memo = [[0] * n for _ in range(n)]

            for y1 in range(n):
                for x1 in range(n):
                    if memo[y1][x1] == 0:
                        continue
                    p = memo[y1][x1] * 0.125
                    for dx, dy in directions:
                        x2, y2 = x1 + dx, y1 + dy
                        if 0 <= x2 < n and 0 <= y2 < n:
                            new_memo[y2][x2] += p

            memo = new_memo

        return sum([sum(r) for r in memo])
