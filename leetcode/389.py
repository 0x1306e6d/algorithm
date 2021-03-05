"""
    File: 389.py
    Title: Find the Difference
    Difficulty: Easy
    URL: https://leetcode.com/problems/find-the-difference/
"""

import unittest


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = list(sorted(s))
        sorted_t = list(sorted(t))
        for i in range(len(s)):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]
        return sorted_t[-1]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "abcd"
        t = "abcde"
        # Output
        output = "e"

        solution = Solution()
        self.assertEqual(solution.findTheDifference(s, t), output)

    def test_example2(self):
        # Input
        s = ""
        t = "y"
        # Output
        output = "y"

        solution = Solution()
        self.assertEqual(solution.findTheDifference(s, t), output)

    def test_example3(self):
        # Input
        s = "a"
        t = "aa"
        # Output
        output = "a"

        solution = Solution()
        self.assertEqual(solution.findTheDifference(s, t), output)

    def test_example3(self):
        # Input
        s = "ae"
        t = "aea"
        # Output
        output = "a"

        solution = Solution()
        self.assertEqual(solution.findTheDifference(s, t), output)


if __name__ == "__main__":
    unittest.main()
