"""
    File: 1260.py
    Title: Shift 2D Grid
    Difficulty: Easy
    URL: https://leetcode.com/problems/shift-2d-grid/
"""

import unittest

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        column_length = len(grid[0])

        flat = []
        for row in grid:
            flat += row

        shift_k = len(flat) - k
        ans = [[] for _ in range(len(grid))]
        for i in range(len(flat)):
            ans[i // column_length].append(flat[(i + shift_k) % len(flat)])
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 1
        # Output
        output = [[9, 1, 2], [3, 4, 5], [6, 7, 8]]

        solution = Solution()
        self.assertEqual(solution.shiftGrid(grid, k), output)

    def test_example2(self):
        # Input
        grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
        k = 4
        # Output
        output = [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]

        solution = Solution()
        self.assertEqual(solution.shiftGrid(grid, k), output)

    def test_example3(self):
        # Input
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 9
        # Output
        output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        solution = Solution()
        self.assertEqual(solution.shiftGrid(grid, k), output)


if __name__ == "__main__":
    unittest.main()
