"""
    File: 521.py
    Title: Longest Uncommon Subsequence I
    Difficulty: Easy
    URL: https://leetcode.com/problems/longest-uncommon-subsequence-i/
"""

import unittest


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a != b:
            return max(len(a), len(b))
        return -1


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        a = "aba"
        b = "cdc"
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.findLUSlength(a, b), output)

    def test_example2(self):
        # Input
        a = "aaa"
        b = "bbb"
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.findLUSlength(a, b), output)


if __name__ == "__main__":
    unittest.main()
