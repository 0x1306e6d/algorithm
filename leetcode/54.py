"""
    File: 54.py
    Title: Spiral Matrix
    Difficulty: Medium
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        m, n = len(matrix), len(matrix[0])

        for r in matrix:
            print(r)

        ans = []
        visited = [[False] * n for _ in range(m)]
        p = (0, 0)
        visited[0][0] = True
        d = 0
        while len(ans) < (m * n):
            x, y = p
            ans.append(matrix[y][x])
            if len(ans) >= m * n:
                break

            xx, yy = x + dx[d], y + dy[d]
            while True:
                if 0 <= xx < n and 0 <= yy < m and not visited[yy][xx]:
                    break
                d = (d + 1) % len(dx)
                xx, yy = x + dx[d], y + dy[d]
            visited[yy][xx] = True
            p = (xx, yy)
        return ans
