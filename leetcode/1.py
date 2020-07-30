"""
    File: 1.py
    Title: Two Sum
    Difficulty: Easy
    URL: https://leetcode.com/problems/two-sum/
"""

import unittest

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)

        for i in range(l):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [2, 7, 11, 15]
        target = 9
        # Output
        output = [0, 1]

        solution = Solution()
        self.assertEqual(solution.twoSum(nums, target), output)


if __name__ == "__main__":
    unittest.main()
