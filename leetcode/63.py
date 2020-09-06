"""
    File: 63.py
    Title: Unique Paths II
    Difficulty: Medium
    URL: https://leetcode.com/problems/unique-paths-ii/
"""

import unittest

from queue import deque
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        height = len(obstacle_grid)
        width = len(obstacle_grid[0])

        if obstacle_grid[0][0] == 1:
            return 0
        if obstacle_grid[height - 1][width - 1] == 1:
            return 0

        __dx__ = [-1, 0]
        __dy__ = [0, -1]

        cache = [[0] * width for _ in range(height)]
        cache[0][0] = 1
        for y in range(height):
            for x in range(width):
                for dx, dy in zip(__dx__, __dy__):
                    pre_x = x + dx
                    pre_y = y + dy
                    if 0 <= pre_x < width and 0 <= pre_y < height:
                        if obstacle_grid[pre_y][pre_x] == 0:
                            cache[y][x] += cache[pre_y][pre_x]
        return cache[height - 1][width - 1]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        obstacle_grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.uniquePathsWithObstacles(obstacle_grid),
                         output)


if __name__ == "__main__":
    unittest.main()
