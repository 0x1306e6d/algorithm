"""
    File: 540.py
    Title: Single Element in a Sorted Array
    Difficulty: Medium
    URL: https://leetcode.com/problems/single-element-in-a-sorted-array/
"""

import unittest

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        previous = None
        for num in nums:
            if previous is None:
                previous = num
            elif previous == num:
                previous = None
            else:
                return previous
        return previous


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.singleNonDuplicate(nums), output)

    def test_example2(self):
        # Input
        nums = [3, 3, 7, 7, 10, 11, 11]
        # Output
        output = 10

        solution = Solution()
        self.assertEqual(solution.singleNonDuplicate(nums), output)


if __name__ == "__main__":
    unittest.main()
