"""
    File: 200.py
    Title: Number of Islands
    Difficulty: Medium
    URL: https://leetcode.com/problems/number-of-islands/
"""

import unittest

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        m = len(grid)
        n = len(grid[0])

        visited = [[False]*n for _ in range(m)]

        def dfs(x: int, y: int) -> None:
            if visited[y][x]:
                return

            visited[y][x] = True
            for dx, dy in d:
                next_x = x + dx
                next_y = y + dy
                if (0 <= next_x < n) and (0 <= next_y < m):
                    if grid[next_y][next_x] == '1':
                        dfs(next_x, next_y)

        islands = 0
        for y in range(m):
            for x in range(n):
                if (grid[y][x] == '1') and (not visited[y][x]):
                    dfs(x, y)
                    islands += 1
        return islands


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.numIslands(grid), output)

    def test_example2(self):
        # Input
        grid = grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.numIslands(grid), output)


if __name__ == "__main__":
    unittest.main()
