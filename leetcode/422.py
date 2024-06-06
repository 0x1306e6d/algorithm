"""
    File: 422.py
    Title: Valid Word Square
    Difficulty: Easy
"""

from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)
        cols = 0
        for word in words:
            cols = max(cols, len(word))

        k = max(rows, cols)
        matrix = [[""] * k for _ in range(k)]
        for i, word in enumerate(words):
            for j, c in enumerate(word):
                matrix[i][j] = c

        for y in range(k):
            for x in range(y):
                if matrix[y][x] != matrix[x][y]:
                    return False
        return True
