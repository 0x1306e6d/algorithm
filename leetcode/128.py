"""
    File: 128.py
    Title: Longest Consecutive Sequence
    Difficulty: Hard
    URL: https://leetcode.com/problems/longest-consecutive-sequence/
"""

import unittest

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive = 0
        longest_consecutive = 0
        previous = 10**9 + 1
        for num in sorted(set(nums)):
            if num == (previous + 1):
                consecutive += 1
            else:
                longest_consecutive = max(longest_consecutive, consecutive)
                consecutive = 1
            previous = num
        return max(longest_consecutive, consecutive)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [100, 4, 200, 1, 3, 2]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.longestConsecutive(nums), output)

    def test_example2(self):
        # Input
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        # Output
        output = 9

        solution = Solution()
        self.assertEqual(solution.longestConsecutive(nums), output)


if __name__ == "__main__":
    unittest.main()
