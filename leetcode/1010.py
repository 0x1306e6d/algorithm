"""
    File: 1010.py
    Title: Pairs of Songs With Total Durations Divisible by 60
    Difficulty: Easy
    URL: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
"""

import unittest

from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hint = defaultdict(int)
        for t in time:
            hint[t % 60] += 1

        count = 0
        for i in range(30 + 1):
            if i == 0 or i == 30:
                count += ((hint[i] * (hint[i] - 1)) // 2)
            else:
                count += (hint[i] * hint[60 - i])
        return count


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        time = [30, 20, 150, 100, 40]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.numPairsDivisibleBy60(time), output)

    def test_example2(self):
        # Input
        time = [60, 60, 60]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.numPairsDivisibleBy60(time), output)


if __name__ == "__main__":
    unittest.main()
