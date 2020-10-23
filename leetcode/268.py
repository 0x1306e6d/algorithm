"""
    File: 268.py
    Title: Missing Number
    Difficulty: Easy
    URL: https://leetcode.com/problems/missing-number/
"""

import unittest

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        as_is = sum(nums)
        to_be = (n * (n + 1)) // 2
        return to_be - as_is


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [3, 0, 1]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.missingNumber(nums), output)

    def test_example2(self):
        # Input
        nums = [0, 1]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.missingNumber(nums), output)

    def test_example3(self):
        # Input
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        # Output
        output = 8

        solution = Solution()
        self.assertEqual(solution.missingNumber(nums), output)

    def test_example4(self):
        # Input
        nums = [0]
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.missingNumber(nums), output)


if __name__ == "__main__":
    unittest.main()
