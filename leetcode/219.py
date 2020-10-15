"""
    File: 219.py
    Title: Contains Duplicate II
    Difficulty: Easy
    URL: https://leetcode.com/problems/contains-duplicate-ii/
"""

import unittest

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dp = {}
        for i in range(len(nums)):
            if nums[i] in dp:
                if i - dp[nums[i]] <= k:
                    return True
                else:
                    dp[nums[i]] = i
            else:
                dp[nums[i]] = i
        return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 2, 3, 1]
        k = 3
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.containsNearbyDuplicate(nums, k), output)

    def test_example2(self):
        # Input
        nums = [1, 0, 1, 1]
        k = 1
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.containsNearbyDuplicate(nums, k), output)

    def test_example3(self):
        # Input
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.containsNearbyDuplicate(nums, k), output)

    def test_example4(self):
        # Input
        nums = [99, 99]
        k = 2
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.containsNearbyDuplicate(nums, k), output)


if __name__ == "__main__":
    unittest.main()
