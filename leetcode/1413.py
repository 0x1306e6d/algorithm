"""
    File: 1413.py
    Title: Minimum Value to Get Positive Step by Step Sum
    Difficulty: Easy
    URL: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
"""

import unittest

from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        step_by_step_sum = 0
        min_step = 0
        for n in nums:
            step_by_step_sum = step_by_step_sum + n
            min_step = min(min_step, step_by_step_sum)
        return max(1, 1 - min_step)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [-3, 2, -3, 4, 2]
        # Output
        output = 5

        solution = Solution()
        self.assertEqual(solution.minStartValue(nums), output)

    def test_example2(self):
        # Input
        nums = [1, 2]
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.minStartValue(nums), output)

    def test_example3(self):
        # Input
        nums = [1, -2, -3]
        # Output
        output = 5

        solution = Solution()
        self.assertEqual(solution.minStartValue(nums), output)


if __name__ == "__main__":
    unittest.main()
