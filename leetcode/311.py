"""
    File: 311.py
    Title: Sparse Matrix Multiplication
    Difficulty: Medium
"""

from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat2), len(mat2[0])

        A = [[] for _ in range(m)]
        for y in range(m):
            for x in range(k):
                if mat1[y][x] != 0:
                    A[y].append((mat1[y][x], x))
        B = [[] for _ in range(k)]
        for y in range(k):
            for x in range(n):
                if mat2[y][x] != 0:
                    B[y].append((mat2[y][x], x))

        ans = [[0] * n for _ in range(m)]
        for y in range(m):
            for v1, x1 in A[y]:
                for v2, x2 in B[x1]:
                    ans[y][x2] += v1 * v2
        return ans
