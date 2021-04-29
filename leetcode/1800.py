"""
    File: 1800.py
    Title: Maximum Ascending Subarray Sum
    Difficulty: Easy
    URL: https://leetcode.com/problems/maximum-ascending-subarray-sum/
"""

import unittest

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0

        ascending = False
        subarray_sum = 0
        previous = 0
        for n in nums:
            if n > previous:
                if not ascending:
                    ascending = True
                subarray_sum += n
            else:
                ascending = False
                ans = max(ans, subarray_sum)
                subarray_sum = n
            previous = n
        ans = max(ans, subarray_sum)

        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [10, 20, 30, 5, 10, 50]
        # Output
        output = 65

        solution = Solution()
        self.assertEqual(solution.maxAscendingSum(nums), output)

    def test_example2(self):
        # Input
        nums = [10, 20, 30, 40, 50]
        # Output
        output = 150

        solution = Solution()
        self.assertEqual(solution.maxAscendingSum(nums), output)

    def test_example3(self):
        # Input
        nums = [12, 17, 15, 13, 10, 11, 12]
        # Output
        output = 33

        solution = Solution()
        self.assertEqual(solution.maxAscendingSum(nums), output)

    def test_example4(self):
        # Input
        nums = [100, 10, 1]
        # Output
        output = 100

        solution = Solution()
        self.assertEqual(solution.maxAscendingSum(nums), output)


if __name__ == "__main__":
    unittest.main()
