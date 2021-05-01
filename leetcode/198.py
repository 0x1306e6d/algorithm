"""
    File: 198.py
    Title: House Robber
    Difficulty: Medium
    URL: https://leetcode.com/problems/house-robber/
"""

import unittest

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = 0
        not_robbed = 0

        for n in nums:
            next_robbed = max(robbed, not_robbed + n)
            not_robbed = max(robbed, not_robbed)
            robbed = next_robbed

        return max(robbed, not_robbed)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 2, 3, 1]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.rob(nums), output)

    def test_example2(self):
        # Input
        nums = [2, 7, 9, 3, 1]
        # Output
        output = 12

        solution = Solution()
        self.assertEqual(solution.rob(nums), output)


if __name__ == "__main__":
    unittest.main()
