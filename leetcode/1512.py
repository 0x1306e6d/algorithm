"""
    File: 1512.py
    Title: Number of Good Pairs
    Difficulty: Easy
    URL: https://leetcode.com/problems/number-of-good-pairs/
"""

import unittest

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 2, 3, 1, 1, 3]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.numIdenticalPairs(nums), output)

    def test_example2(self):
        # Input
        nums = [1, 1, 1, 1]
        # Output
        output = 6

        solution = Solution()
        self.assertEqual(solution.numIdenticalPairs(nums), output)

    def test_example3(self):
        # Input
        nums = [1, 2, 3]
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.numIdenticalPairs(nums), output)


if __name__ == "__main__":
    unittest.main()
