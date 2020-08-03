"""
    File: 169.py
    Title: Majority Element
    Difficulty: Easy
    URL: https://leetcode.com/problems/majority-element/
"""

import unittest

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return sorted_d[0][0]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [3, 2, 3]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.majorityElement(nums), output)

    def test_example2(self):
        # Input
        nums = [2, 2, 1, 1, 1, 2, 2]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.majorityElement(nums), output)


if __name__ == "__main__":
    unittest.main()
