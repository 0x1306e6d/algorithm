"""
    File: 1689.py
    Title: Partitioning Into Minimum Number Of Deci-Binary Numbers
    Difficulty: Medium
"""

import unittest


class Solution:
    def minPartitions(self, n: str) -> int:
        maximum = 0
        for c in n:
            maximum = max(maximum, int(c))
        return maximum


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = "32"
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.minPartitions(n), output)

    def test_example2(self):
        # Input
        n = "82734"
        # Output
        output = 8

        solution = Solution()
        self.assertEqual(solution.minPartitions(n), output)

    def test_example3(self):
        # Input
        n = "27346209830709182346"
        # Output
        output = 9

        solution = Solution()
        self.assertEqual(solution.minPartitions(n), output)


if __name__ == "__main__":
    unittest.main()
