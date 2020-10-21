"""
    File: 442.py
    Title: Find All Duplicates in an Array
    Difficulty: Medium
    URL: https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""

import unittest

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicated = []
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            if nums[j] < 0:
                duplicated.append(abs(nums[i]))
            nums[j] = -nums[j]
        return sorted(duplicated)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        # Output
        output = [2, 3]

        solution = Solution()
        self.assertEqual(solution.findDuplicates(nums), output)


if __name__ == "__main__":
    unittest.main()
