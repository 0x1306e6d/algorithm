"""
    File: 1503.py
    Title: Last Moment Before All Ants Fall Out of a Plank
    Difficulty: Medium
    URL: https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
"""

import unittest

from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        right = list(map(lambda x: n - x, right))
        return max(left + right)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 4
        left = [4, 3]
        right = [0, 1]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.getLastMoment(n, left, right), output)

    def test_example2(self):
        # Input
        n = 7
        left = []
        right = [0, 1, 2, 3, 4, 5, 6, 7]
        # Output
        output = 7

        solution = Solution()
        self.assertEqual(solution.getLastMoment(n, left, right), output)

    def test_example3(self):
        # Input
        n = 7
        left = [0, 1, 2, 3, 4, 5, 6, 7]
        right = []
        # Output
        output = 7

        solution = Solution()
        self.assertEqual(solution.getLastMoment(n, left, right), output)

    def test_example4(self):
        # Input
        n = 9
        left = [5]
        right = [4]
        # Output
        output = 5

        solution = Solution()
        self.assertEqual(solution.getLastMoment(n, left, right), output)

    def test_example5(self):
        # Input
        n = 6
        left = [6]
        right = [0]
        # Output
        output = 6

        solution = Solution()
        self.assertEqual(solution.getLastMoment(n, left, right), output)


if __name__ == "__main__":
    unittest.main()
