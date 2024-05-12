"""
    File: 1770.py
    Title: Maximum Score from Performing Multiplication Operations
    Difficulty: Hard
    URL: https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
"""

import unittest

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        self.memo = {}

        def dp(s, e, i):
            if (s, e) in self.memo:
                return self.memo[(s, e)]
            if i == m - 1:
                self.memo[(s, e)] = max(
                    nums[s] * multipliers[i],
                    nums[e] * multipliers[i],
                )
            else:
                self.memo[(s, e)] = max(
                    nums[s] * multipliers[i] + dp(s + 1, e, i + 1),
                    nums[e] * multipliers[i] + dp(s, e - 1, i + 1),
                )
            return self.memo[(s, e)]

        return dp(0, n - 1, 0)


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
