"""
    File: 561.py
    Title: Array Partition I
    Difficulty: Easy
    URL: https://leetcode.com/problems/array-partition-i/
"""

import unittest

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = list(sorted(nums))

        ans = 0
        for i in range(0, len(sorted_nums), 2):
            ans += sorted_nums[i]
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 4, 3, 2]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.arrayPairSum(nums), output)

    def test_example2(self):
        # Input
        nums = [6, 2, 6, 5, 1, 2]
        # Output
        output = 9

        solution = Solution()
        self.assertEqual(solution.arrayPairSum(nums), output)


if __name__ == "__main__":
    unittest.main()
