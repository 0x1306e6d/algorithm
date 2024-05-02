"""
    File: 1631.py
    Title: Path With Minimum Effort
    Difficulty: Medium
    URL: https://leetcode.com/problems/path-with-minimum-effort/
"""

import unittest

from collections import deque
from typing import List

__dx__ = [0, 0, -1, 1]
__dy__ = [-1, 1, 0, 0]


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        columns = len(heights[0])

        memo = [[987654321] * columns for _ in range(rows)]

        q = deque()
        q.append((0, 0, 0))
        memo[0][0] = 0
        while q:
            x, y, effort = q.popleft()

            for dx, dy in zip(__dx__, __dy__):
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < columns and 0 <= new_y < rows:
                    effort_here = abs(heights[y][x] - heights[new_y][new_x])
                    effort_here = max(effort, effort_here)
                    if effort_here < memo[new_y][new_x]:
                        memo[new_y][new_x] = effort_here
                        q.append((new_x, new_y, effort_here))
        return memo[rows - 1][columns - 1]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.minimumEffortPath(heights), output)

    def test_example2(self):
        # Input
        heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.minimumEffortPath(heights), output)

    def test_example3(self):
        # Input
        heights = [
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1],
        ]
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.minimumEffortPath(heights), output)


if __name__ == "__main__":
    unittest.main()
