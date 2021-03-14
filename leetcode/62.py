"""
    File: 62.py
    Title: Unique Paths
    Difficulty: Medium
    URL: https://leetcode.com/problems/unique-paths/
"""

import unittest


class Solution:
    def __init__(self):
        self.cache = {}

    def uniquePaths(self, m: int, n: int) -> int:
        return self.comb(m + n - 2, m - 1)

    def comb(self, n: int, r: int) -> int:
        if n in self.cache:
            if r in self.cache[n]:
                return self.cache[n][r]
        else:
            self.cache[n] = {}

        if n == r or r == 0:
            return 1
        self.cache[n][r] = self.comb(n - 1, r - 1) + self.comb(n - 1, r)
        return self.cache[n][r]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        m = 3
        n = 7
        # Output
        output = 28

        solution = Solution()
        self.assertEqual(solution.uniquePaths(m, n), output)

    def test_example2(self):
        # Input
        m = 3
        n = 2
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.uniquePaths(m, n), output)

    def test_example3(self):
        # Input
        m = 7
        n = 3
        # Output
        output = 28

        solution = Solution()
        self.assertEqual(solution.uniquePaths(m, n), output)

    def test_example4(self):
        # Input
        m = 3
        n = 3
        # Output
        output = 6

        solution = Solution()
        self.assertEqual(solution.uniquePaths(m, n), output)


if __name__ == "__main__":
    unittest.main()
