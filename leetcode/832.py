"""
    File: 832.py
    Title: Flipping an Image
    Difficulty: Easy
    URL: https://leetcode.com/problems/flipping-an-image/
"""

import unittest

from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def inverted(a: List[int]):
            for i in a:
                if i == 1:
                    yield 0
                else:
                    yield 1
        return [list(inverted(reversed(row))) for row in A]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
        # Output
        output = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

        solution = Solution()
        self.assertEqual(solution.flipAndInvertImage(A), output)

    def test_example2(self):
        # Input
        A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
        # Output
        output = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]

        solution = Solution()
        self.assertEqual(solution.flipAndInvertImage(A), output)


if __name__ == "__main__":
    unittest.main()
