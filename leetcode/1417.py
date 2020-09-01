"""
    File: 1417.py
    Title: Reformat The String
    Difficulty: Easy
    URL: https://leetcode.com/problems/reformat-the-string/
"""

import unittest

from typing import List


class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []
        for c in s:
            if 'a' <= c <= 'z':
                letters.append(c)
            elif '0' <= c <= '9':
                digits.append(c)

        if abs(len(letters) - len(digits)) <= 1:
            return self.make_permutation(letters, digits)
        else:
            return ""

    def make_permutation(self, first: List[str], second: List[str]):
        if len(first) < len(second):
            return self.make_permutation(second, first)

        permutation = ""
        i = 0
        while i < len(second):
            permutation += "{}{}".format(first[i], second[i])
            i += 1
        while i < len(first):
            permutation += first[i]
            i += 1
        return permutation


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "a0b1c2"
        # Output
        output = "a0b1c2"

        solution = Solution()
        self.assertEqual(solution.reformat(s), output)

    def test_example2(self):
        # Input
        s = "leetcode"
        # Output
        output = ""

        solution = Solution()
        self.assertEqual(solution.reformat(s), output)

    def test_example3(self):
        # Input
        s = "1229857369"
        # Output
        output = ""

        solution = Solution()
        self.assertEqual(solution.reformat(s), output)

    def test_example4(self):
        # Input
        s = "covid2019"
        # Output
        output = "c2o0v1i9d"

        solution = Solution()
        self.assertEqual(solution.reformat(s), output)

    def test_example5(self):
        # Input
        s = "ab123"
        # Output
        output = "1a2b3"

        solution = Solution()
        self.assertEqual(solution.reformat(s), output)


if __name__ == "__main__":
    unittest.main()
