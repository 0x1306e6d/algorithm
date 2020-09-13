"""
    File: 991.py
    Title: Broken Calculator
    Difficulty: Medium
    URL: https://leetcode.com/problems/broken-calculator/
"""

import unittest


class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        if x > y:
            return x - y
        if x == y:
            return 0

        count = 0
        while x < y:
            if (y % 2) == 1:
                y += 1
            else:
                y //= 2
            count += 1
        return count + (x - y)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        X = 2
        Y = 3
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.brokenCalc(X, Y), output)

    def test_example2(self):
        # Input
        X = 5
        Y = 8
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.brokenCalc(X, Y), output)

    def test_example3(self):
        # Input
        X = 3
        Y = 10
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.brokenCalc(X, Y), output)

    def test_example4(self):
        # Input
        X = 1024
        Y = 1
        # Output
        output = 1023

        solution = Solution()
        self.assertEqual(solution.brokenCalc(X, Y), output)


if __name__ == "__main__":
    unittest.main()
