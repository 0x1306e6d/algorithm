"""
    File: 1337.py
    Title: The K Weakest Rows in a Matrix
    Difficulty: Easy
    URL: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""

import unittest

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for i, row in enumerate(mat):
            soldiers = row.count(1)
            rows.append((soldiers, i))

        ordered = list(map(lambda pair: pair[1], sorted(rows)))
        return ordered[:k]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        mat = [[1, 1, 0, 0, 0],
               [1, 1, 1, 1, 0],
               [1, 0, 0, 0, 0],
               [1, 1, 0, 0, 0],
               [1, 1, 1, 1, 1]]
        k = 3
        # Output
        output = [2, 0, 3]

        solution = Solution()
        self.assertEqual(solution.kWeakestRows(mat, k), output)

    def test_example2(self):
        # Input
        mat = [[1, 0, 0, 0],
               [1, 1, 1, 1],
               [1, 0, 0, 0],
               [1, 0, 0, 0]]
        k = 2
        # Output
        output = [0, 2]

        solution = Solution()
        self.assertEqual(solution.kWeakestRows(mat, k), output)


if __name__ == "__main__":
    unittest.main()
