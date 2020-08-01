"""
    File: 397.py
    Title: Integer Replacement
    Difficulty: Medium
    URL: https://leetcode.com/problems/integer-replacement/
"""

import unittest


class Solution:
    def __init__(self):
        self.dp = {}

    def integerReplacement(self, n: int) -> int:
        return self.replace(n)

    def replace(self, m: int):
        if m in self.dp:
            return self.dp[m]

        if m == 1:
            return 0

        if m % 2 == 0:
            self.dp[m] = 1 + self.replace(m // 2)
        else:
            self.dp[m] = 1 + min(self.replace(m + 1), self.replace(m - 1))
        return self.dp[m]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 8
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.integerReplacement(n), output)

    def test_example2(self):
        # Input
        n = 7
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.integerReplacement(n), output)


if __name__ == "__main__":
    unittest.main()
