"""
    File: 1030.py
    Title: Matrix Cells in Distance Order
    Difficulty: Easy
    URL: https://leetcode.com/problems/matrix-cells-in-distance-order/
"""

import unittest

from collections import deque
from typing import List


class Solution:
    def allCellsDistOrder(self,
                          rows: int,
                          cols: int,
                          rCenter: int,
                          cCenter: int) -> List[List[int]]:
        __dr__ = [-1, 0, 1, 0]
        __dc__ = [0, -1, 0, 1]

        visited = [[False] * cols for _ in range(rows)]
        visited[rCenter][cCenter] = True

        cells = []
        q = deque()
        q.append((rCenter, cCenter))
        visited[rCenter][cCenter] = True
        while q:
            r, c = q.popleft()
            cells.append([r, c])

            for dr, dc in zip(__dr__, __dc__):
                nr = r + dr
                nc = c + dc
                if (0 <= nc < cols) and (0 <= nr < rows):
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
        return cells


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        rows = 1
        cols = 2
        rCenter = 0
        cCenter = 0
        # Output
        output = [[0, 0], [0, 1]]

        solution = Solution()
        self.assertEqual(solution.allCellsDistOrder(rows,
                                                    cols,
                                                    rCenter,
                                                    cCenter),
                         output)

    def test_example2(self):
        # Input
        rows = 2
        cols = 2
        rCenter = 0
        cCenter = 1
        # Output
        output = [[0, 1], [0, 0], [1, 1], [1, 0]]

        solution = Solution()
        self.assertEqual(solution.allCellsDistOrder(rows,
                                                    cols,
                                                    rCenter,
                                                    cCenter),
                         output)

    def test_example3(self):
        # Input
        rows = 2
        cols = 3
        rCenter = 1
        cCenter = 2
        # Output
        output = [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]

        solution = Solution()
        self.assertEqual(solution.allCellsDistOrder(rows,
                                                    cols,
                                                    rCenter,
                                                    cCenter),
                         output)


if __name__ == "__main__":
    unittest.main()
