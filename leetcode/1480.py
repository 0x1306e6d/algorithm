"""
    File: 1480.py
    Title: Running Sum of 1d Array
    Difficulty: Easy
    URL: https://leetcode.com/problems/running-sum-of-1d-array/
"""

import unittest

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        for i, n in enumerate(nums):
            if i == 0:
                arr.append(n)
            else:
                arr.append(arr[i - 1] + n)
        return arr


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 2, 3, 4]
        # Output
        output = [1, 3, 6, 10]

        solution = Solution()
        self.assertEqual(solution.runningSum(nums), output)

    def test_example2(self):
        # Input
        nums = [1, 1, 1, 1, 1]
        # Outpu
        output = [1, 2, 3, 4, 5]

        solution = Solution()
        self.assertEqual(solution.runningSum(nums), output)

    def test_example3(self):
        # Input
        nums = [3, 1, 2, 10, 1]
        # Output
        output = [3, 4, 6, 16, 17]

        solution = Solution()
        self.assertEqual(solution.runningSum(nums), output)


if __name__ == "__main__":
    unittest.main()
