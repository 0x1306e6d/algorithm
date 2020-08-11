"""
    File: 1394.py
    Title: Find Lucky Integer in an Array
    Difficulty: Easy
    URL: https://leetcode.com/problems/find-lucky-integer-in-an-array/
"""

import unittest

from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        table = {}
        for n in arr:
            if n not in table:
                table[n] = 1
            else:
                table[n] += 1

        for k, v in sorted(table.items(), reverse=True):
            if k == v:
                return k
        return -1


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        arr = [2, 2, 3, 4]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.findLucky(arr), output)

    def test_example2(self):
        # Input
        arr = [1, 2, 2, 3, 3, 3]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.findLucky(arr), output)

    def test_example3(self):
        # Input
        arr = [2, 2, 2, 3, 3]
        # Output
        output = -1

        solution = Solution()
        self.assertEqual(solution.findLucky(arr), output)

    def test_example4(self):
        # Input
        arr = [5]
        # Output
        output = -1

        solution = Solution()
        self.assertEqual(solution.findLucky(arr), output)

    def test_example5(self):
        # Input
        arr = [7, 7, 7, 7, 7, 7, 7]
        # Output
        output = 7

        solution = Solution()
        self.assertEqual(solution.findLucky(arr), output)


if __name__ == "__main__":
    unittest.main()
