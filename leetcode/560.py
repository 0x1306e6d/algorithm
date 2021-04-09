"""
    File: 560.py
    Title: Subarray Sum Equals K
    Difficulty: Medium
    URL: https://leetcode.com/problems/subarray-sum-equals-k/
"""

import unittest

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {}

        count = 0
        s = 0
        for n in nums:
            s += n
            if s == k:
                count += 1
            if s - k in memo:
                count += memo[s - k]
            if s not in memo:
                memo[s] = 0
            memo[s] += 1
        return count


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 1, 1]
        k = 2
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.subarraySum(nums, k), output)

    def test_example2(self):
        # Input
        nums = [1, 2, 3]
        k = 3
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.subarraySum(nums, k), output)


if __name__ == "__main__":
    unittest.main()
