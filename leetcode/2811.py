"""
    File: 2811.py
    Title: Check if it is Possible to Split Array
    Difficulty: Medium
"""

import unittest

from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) <= 2:
            return True
        for i in range(0, len(nums) - 1):
            if nums[i] + nums[i + 1] >= m:
                return True
        return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [2, 2, 1]
        m = 4
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.canSplitArray(nums, m), output)

    def test_example2(self):
        # Input
        nums = [2, 1, 3]
        m = 5
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.canSplitArray(nums, m), output)

    def test_example3(self):
        # Input
        nums = [2, 3, 3, 2, 3]
        m = 6
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.canSplitArray(nums, m), output)


if __name__ == "__main__":
    unittest.main()
