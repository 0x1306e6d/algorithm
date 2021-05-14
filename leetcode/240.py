"""
    File: 240.py
    Title: Search a 2D Matrix II
    Difficulty: Medium
    URL: https://leetcode.com/problems/search-a-2d-matrix-ii/
"""

import unittest

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = m - 1
        while (i < n) and (j >= 0):
            if matrix[j][i] == target:
                return True
            if matrix[j][i] > target:
                j -= 1
            else:
                i += 1
        return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        matrix = [[1, 4, 7, 11, 15],
                  [2, 5, 8, 12, 19],
                  [3, 6, 9, 16, 22],
                  [10, 13, 14, 17, 24],
                  [18, 21, 23, 26, 30]]
        target = 5
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.searchMatrix(matrix, target), output)

    def test_example2(self):
        # Input
        matrix = [[1, 4, 7, 11, 15],
                  [2, 5, 8, 12, 19],
                  [3, 6, 9, 16, 22],
                  [10, 13, 14, 17, 24],
                  [18, 21, 23, 26, 30]]
        target = 20
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.searchMatrix(matrix, target), output)


if __name__ == "__main__":
    unittest.main()
