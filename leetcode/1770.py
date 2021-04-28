"""
    File: 1770.py
    Title: Maximum Score from Performing Multiplication Operations
    Difficulty: Medium
    URL: https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
"""

import unittest

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)

        memo = {}

        def operate(start: int, i: int) -> int:
            if i >= m:
                return 0

            if start not in memo:
                memo[start] = {}
            if i in memo[start]:
                return memo[start][i]

            end = n - (i - start) - 1
            s = operate(start + 1, i + 1) + (nums[start] * multipliers[i])
            e = operate(start, i + 1) + (nums[end] * multipliers[i])
            memo[start][i] = max(s, e)
            return memo[start][i]

        return operate(0, 0)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 2, 3]
        multipliers = [3, 2, 1]
        # Output
        output = 14

        solution = Solution()
        self.assertEqual(solution.maximumScore(nums, multipliers), output)

    def test_example2(self):
        # Input
        nums = [-5, -3, -3, -2, 7, 1]
        multipliers = [-10, -5, 3, 4, 6]
        # Output
        output = 102

        solution = Solution()
        self.assertEqual(solution.maximumScore(nums, multipliers), output)


if __name__ == "__main__":
    unittest.main()
