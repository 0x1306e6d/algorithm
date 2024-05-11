"""
    File: 399.py
    Title: Evaluate Division
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        chars = set()
        matrix = {}
        for (a, b), v in zip(equations, values):
            chars.add(a)
            chars.add(b)
            if a not in matrix:
                matrix[a] = {}
            if b not in matrix:
                matrix[b] = {}
            matrix[a][b] = v
            matrix[b][a] = 1 / v

        for a in matrix:
            q = deque()
            for u in matrix[a]:
                q.append(u)
            while q:
                u = q.pop()
                for v in matrix[u]:
                    if v in matrix[a]:
                        continue
                    matrix[a][v] = matrix[a][u] * matrix[u][v]
                    q.append(v)

        ans = []
        for a, b in queries:
            if a not in chars or b not in chars:
                ans.append(-1)
                continue
            if b in matrix[a]:
                ans.append(matrix[a][b])
            else:
                ans.append(-1)
        return ans
