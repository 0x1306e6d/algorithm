"""
    File: 665.py
    Title: Non-decreasing Array
    Difficulty: Medium
    URL: https://leetcode.com/problems/non-decreasing-array/
"""

import unittest

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        first = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if first:
                    first = False

                    if i > 1:
                        if nums[i - 2] > nums[i]:
                            nums[i] = nums[i - 1]
                else:
                    return False
        return True


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [4, 2, 3]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.checkPossibility(nums), output)

    def test_example2(self):
        # Input
        nums = [4, 2, 1]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.checkPossibility(nums), output)


if __name__ == "__main__":
    unittest.main()
