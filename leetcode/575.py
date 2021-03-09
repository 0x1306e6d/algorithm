"""
    File: 575.py
    Title: Distribute Candies
    Difficulty: Easy
    URL: https://leetcode.com/problems/distribute-candies/
"""

import unittest

from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        candyType = [1, 1, 2, 2, 3, 3]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.distributeCandies(candyType), output)

    def test_example2(self):
        # Input
        candyType = [1, 1, 2, 3]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.distributeCandies(candyType), output)

    def test_example3(self):
        # Input
        candyType = [6, 6, 6, 6]
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.distributeCandies(candyType), output)


if __name__ == "__main__":
    unittest.main()
