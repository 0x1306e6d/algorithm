"""
    File: 525.py
    Title: Contiguous Array
    Difficulty: Medium
    URL: https://leetcode.com/problems/contiguous-array/
"""

import unittest

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0

        start = {0: 0}
        current = 0
        for i, n in enumerate(nums):
            if n == 0:
                current += 1
            else:
                current -= 1

            if current not in start:
                start[current] = i + 1
            else:
                max_length = max(max_length, i - start[current] + 1)

        return max_length


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [0, 1]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.findMaxLength(nums), output)

    def test_example2(self):
        # Input
        nums = [0, 1, 0]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.findMaxLength(nums), output)


if __name__ == "__main__":
    unittest.main()
