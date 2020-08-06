"""
    File: 1523.py
    Title: Count Odd Numbers in an Interval Range
    Difficulty: Easy
    URL: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
"""

import unittest


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        edge = 1 if ((low % 2) == 1 or (high % 2) == 1) else 0
        return ((high - low) // 2) + edge


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        low = 3
        high = 7
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.countOdds(low, high), output)

    def test_example2(self):
        # Input
        low = 8
        high = 10
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.countOdds(low, high), output)


if __name__ == "__main__":
    unittest.main()
