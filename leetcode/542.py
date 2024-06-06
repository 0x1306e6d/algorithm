"""
    File: 542.py
    Title: 01 Matrix
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        q = deque()
        for y in range(m):
            for x in range(n):
                if mat[y][x] == 0:
                    q.append((x, y, 0))

        ans = [[0] * n for _ in range(m)]
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while q:
            x1, y1, count = q.popleft()

            for dx, dy in directions:
                x2, y2 = x1 + dx, y1 + dy
                if 0 <= x2 < n and 0 <= y2 < m:
                    if mat[y2][x2] == 0:
                        continue
                    mat[y2][x2] = 0

                    ans[y2][x2] = count + 1
                    q.append((x2, y2, count + 1))
        return ans
