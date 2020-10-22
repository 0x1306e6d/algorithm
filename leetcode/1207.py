"""
    File: 1207.py
    Title: Unique Number of Occurrences
    Difficulty: Easy
    URL: https://leetcode.com/problems/unique-number-of-occurrences/
"""

import unittest

from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = defaultdict(int)
        for n in arr:
            occurrences[n] += 1
        number_of_occurrences = occurrences.values()
        return len(number_of_occurrences) == len(set(number_of_occurrences))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        arr = [1, 2, 2, 1, 1, 3]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.uniqueOccurrences(arr), output)

    def test_example2(self):
        # Input
        arr = [1, 2]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.uniqueOccurrences(arr), output)

    def test_example3(self):
        # Input
        arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.uniqueOccurrences(arr), output)


if __name__ == "__main__":
    unittest.main()
