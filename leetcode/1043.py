"""
    File: 1043.py
    Title: Partition Array for Maximum Sum
    Difficulty: Medium
    URL: https://leetcode.com/problems/partition-array-for-maximum-sum/
"""

import unittest

from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = [0] * (len(arr) + 1)
        for i in range(len(arr) + 1):
            maximum = -1
            for j in range(1, min(k, i) + 1):
                maximum = max(maximum, arr[i - j])
                memo[i] = max(memo[i], memo[i - j] + maximum * j)
        return memo[len(arr)]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        arr = [1, 15, 7, 9, 2, 5, 10]
        k = 3
        # Output
        output = 84

        solution = Solution()
        self.assertEqual(solution.maxSumAfterPartitioning(arr, k), output)

    def test_example2(self):
        # Input
        arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
        k = 4
        # Output
        output = 83

        solution = Solution()
        self.assertEqual(solution.maxSumAfterPartitioning(arr, k), output)

    def test_example3(self):
        # Input
        arr = [1]
        k = 1
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.maxSumAfterPartitioning(arr, k), output)


if __name__ == "__main__":
    unittest.main()
