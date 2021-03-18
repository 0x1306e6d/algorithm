"""
    File: 118.py
    Title:  Pascal's Triangle
    Difficulty: Easy
    URL: https://leetcode.com/problems/pascals-triangle/
"""

import unittest

from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        rows = [[1]]

        for i in range(1, num_rows):
            row = []

            above = rows[i - 1]
            for j, n in enumerate(above):
                if j == 0:
                    row.append(n)
                else:
                    row.append(n + above[j - 1])
            row.append(1)

            rows.append(row)

        return rows


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        num_rows = 5
        # Output
        output = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

        solution = Solution()
        self.assertEqual(solution.generate(num_rows), output)

    def test_example2(self):
        # Input
        num_rows = 1
        # Output
        output = [[1]]

        solution = Solution()
        self.assertEqual(solution.generate(num_rows), output)


if __name__ == "__main__":
    unittest.main()
