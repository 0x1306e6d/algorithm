"""
    File: 463.py
    Title: Island Perimeter
    Difficulty: Easy
    URL: https://leetcode.com/problems/island-perimeter/
"""

import unittest

from collections import deque
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        row = len(grid)
        col = len(grid[0])

        def perimeter(i: int, j: int) -> int:
            perimeter = 0

            visited = [[False] * col for _ in range(row)]
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            while q:
                p = q.popleft()

                for dx, dy in d:
                    x, y = (p[1] + dx), (p[0] + dy)
                    if (0 <= x < col) and (0 <= y < row):
                        if grid[y][x] == 1:
                            if not visited[y][x]:
                                visited[y][x] = True
                                q.append((y, x))
                        else:
                            perimeter += 1
                    else:
                        perimeter += 1
            return perimeter

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return perimeter(i, j)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        # Output
        output = 16

        solution = Solution()
        self.assertEqual(solution.islandPerimeter(grid), output)

    def test_example2(self):
        # Input
        grid = [[1]]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.islandPerimeter(grid), output)

    def test_example3(self):
        # Input
        grid = [[1, 0]]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.islandPerimeter(grid), output)


if __name__ == "__main__":
    unittest.main()
