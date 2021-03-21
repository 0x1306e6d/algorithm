"""
    File: 961.py
    Title: N-Repeated Element in Size 2N Array
    Difficulty: Easy
    URL: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
"""

import unittest

from typing import List


class Solution:
    def repeatedNTimes(self, a: List[int]) -> int:
        visited = {}
        for n in a:
            if n in visited:
                return n
            visited[n] = True


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        a = [1, 2, 3, 3]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.repeatedNTimes(a), output)

    def test_example2(self):
        # Input
        a = [2, 1, 2, 5, 3, 2]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.repeatedNTimes(a), output)

    def test_example3(self):
        # Input
        a = [5, 1, 5, 2, 5, 3, 5, 4]
        # Output
        output = 5

        solution = Solution()
        self.assertEqual(solution.repeatedNTimes(a), output)


if __name__ == "__main__":
    unittest.main()
