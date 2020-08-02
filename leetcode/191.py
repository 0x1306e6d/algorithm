"""
    File: 191.py
    Title: Number of 1 Bits
    Difficulty: Easy
    URL: https://leetcode.com/problems/number-of-1-bits/
"""

import unittest


class Solution:
    def hammingWeight(self, n: int) -> int:
        m = n
        weight = 0
        while m > 0:
            if (m % 2) == 1:
                weight += 1
            m //= 2
        return weight


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 11
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.hammingWeight(n), output)

    def test_example2(self):
        # Input
        n = 128
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.hammingWeight(n), output)

    def test_example3(self):
        # Input
        n = 4294967293
        # Output
        output = 31

        solution = Solution()
        self.assertEqual(solution.hammingWeight(n), output)


if __name__ == "__main__":
    unittest.main()
