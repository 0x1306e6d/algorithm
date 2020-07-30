"""
    File: 215.py
    Title: Kth Largest Element in an Array
    Difficulty: Medium
    URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

import unittest

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return list(sorted(nums, reverse=True))[k - 1]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        # Output
        output = 5

        solution = Solution()
        self.assertEqual(solution.findKthLargest(nums, k), output)

    def test_example2(self):
        # Input
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.findKthLargest(nums, k), output)


if __name__ == "__main__":
    unittest.main()
