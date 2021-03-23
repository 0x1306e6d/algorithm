"""
    File: 300.py
    Title: Longest Increasing Subsequence
    Difficulty: Medium
    URL: https://leetcode.com/problems/longest-increasing-subsequence/
"""

import unittest

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for n in nums:
            if (not lis) or (n > lis[-1]):
                lis.append(n)
            else:
                i = self.lower_bound(lis, n)
                lis[i] = n

        return len(lis)

    def lower_bound(self, nums: List[int], n: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2
            if nums[mid] < n:
                low = mid + 1
            else:
                high = mid

        return low


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.lengthOfLIS(nums), output)

    def test_example2(self):
        # Input
        nums = [0, 1, 0, 3, 2, 3]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.lengthOfLIS(nums), output)

    def test_example3(self):
        # Input
        nums = [7, 7, 7, 7, 7, 7, 7]
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.lengthOfLIS(nums), output)


if __name__ == "__main__":
    unittest.main()
