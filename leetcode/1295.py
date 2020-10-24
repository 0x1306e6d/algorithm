"""
    File: 1295.py
    Title: Find Numbers with Even Number of Digits
    Difficulty: Easy
    URL: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""

import unittest

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if (len(list(str(num))) % 2) == 0:
                count += 1
        return count


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [12, 345, 2, 6, 7896]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.findNumbers(nums), output)

    def test_example2(self):
        # Input
        nums = [555, 901, 482, 1771]
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.findNumbers(nums), output)


if __name__ == "__main__":
    unittest.main()
