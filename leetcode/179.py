"""
    File: 179.py
    Title: Largest Number
    Difficulty: Medium
    URL: https://leetcode.com/problems/largest-number/
"""

import unittest

from functools import reduce
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest = reduce(lambda cur, acc: cur + acc,
                         sorted(map(str, nums),
                                key=lambda x: x * 10,
                                reverse=True),
                         "")
        if largest[0] == "0":
            return "0"
        return largest


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [10, 2]
        # Output
        output = "210"

        solution = Solution()
        self.assertEqual(solution.largestNumber(nums), output)

    def test_example2(self):
        # Input
        nums = [3, 30, 34, 5, 9]
        # Output
        output = "9534330"

        solution = Solution()
        self.assertEqual(solution.largestNumber(nums), output)

    def test_example3(self):
        # Input
        nums = [1]
        # Output
        output = "1"

        solution = Solution()
        self.assertEqual(solution.largestNumber(nums), output)

    def test_example4(self):
        # Input
        nums = [10]
        # Output
        output = "10"

        solution = Solution()
        self.assertEqual(solution.largestNumber(nums), output)


if __name__ == "__main__":
    unittest.main()
