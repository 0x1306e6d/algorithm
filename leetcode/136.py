"""
    File: 136.py
    Title: Single Number
    Difficulty: Easy
    URL: https://leetcode.com/problems/single-number/
"""

import unittest

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return s.pop()


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [2, 2, 1]
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.singleNumber(nums), output)

    def test_example2(self):
        # Input
        nums = [4, 1, 2, 1, 2]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.singleNumber(nums), output)


if __name__ == "__main__":
    unittest.main()
