"""
    File: 1122.py
    Title: Relative Sort Array
    Difficulty: Easy
    URL: https://leetcode.com/problems/relative-sort-array/
"""

import unittest

from collections import defaultdict
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = defaultdict(int)
        for n in arr1:
            counts[n] += 1

        ans = []
        for n in arr2:
            ans += ([n] * counts[n])
            del counts[n]
        for n in sorted(counts):
            ans += ([n] * counts[n])
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
        arr2 = [2, 1, 4, 3, 9, 6]
        # Output
        output = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]

        solution = Solution()
        self.assertEqual(solution.relativeSortArray(arr1, arr2), output)


if __name__ == "__main__":
    unittest.main()
