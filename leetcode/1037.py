"""
    File: 1037.py
    Title: Valid Boomerang
    Difficulty: Easy
    URL: https://leetcode.com/problems/valid-boomerang/
"""

import unittest

from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a, b, c = points[0], points[1], points[2]

        if (a == b) or (b == c) or (a == c):
            return False

        a_b = self.gradient(a, b)
        b_c = self.gradient(b, c)
        a_c = self.gradient(c, a)

        return (a_b != b_c) or (b_c != a_c) or (a_b != a_c)

    def gradient(self, a: List[int], b: List[int]) -> float:
        if a[0] == b[0]:
            return 1.0
        elif a[1] == b[1]:
            return 0.0
        return (a[0] - b[0]) / (a[1] - b[1])


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        points = [[1, 1], [2, 3], [3, 2]]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isBoomerang(points), output)

    def test_example2(self):
        # Input
        points = [[1, 1], [2, 2], [3, 3]]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isBoomerang(points), output)


if __name__ == "__main__":
    unittest.main()
