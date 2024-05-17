"""
    File: 48.py
    Title: Rotate Image
    Difficulty: Medium
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1:
            return matrix

        for s in range(len(matrix) // 2):
            start, end = s, len(matrix) - s - 1
            for _ in range(end - start):
                prev = matrix[s + 1][s]
                for x in range(start, end + 1):
                    curr = matrix[start][x]
                    matrix[start][x] = prev
                    prev = curr
                for y in range(start + 1, end + 1):
                    curr = matrix[y][end]
                    matrix[y][end] = prev
                    prev = curr
                for x in range(end - 1, start - 1, -1):
                    curr = matrix[end][x]
                    matrix[end][x] = prev
                    prev = curr
                for y in range(end - 1, start - 1, -1):
                    curr = matrix[y][start]
                    matrix[y][start] = prev
                    prev = curr
