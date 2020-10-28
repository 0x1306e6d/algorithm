"""
    File: 509.py
    Title: Fibonacci Number
    Difficulty: Easy
    URL: https://leetcode.com/problems/fibonacci-number/
"""

import unittest


class Solution:
    def fib(self, n: int) -> int:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 2
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.fib(n), output)

    def test_example2(self):
        # Input
        n = 3
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.fib(n), output)

    def test_example3(self):
        # Input
        n = 4
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.fib(n), output)

    def test_example4(self):
        # Input
        n = 30
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.fib(n), output)


if __name__ == "__main__":
    unittest.main()
