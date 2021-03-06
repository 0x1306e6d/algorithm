"""
    File: 1002.py
    Title: Find Common Characters
    Difficulty: Easy
    URL: https://leetcode.com/problems/find-common-characters/
"""

import unittest

from string import ascii_lowercase
from sys import maxsize
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        characterized_a = []
        for a in A:
            chars = {}

            for c in sorted(a):
                if c not in chars:
                    chars[c] = 0
                chars[c] += 1

            characterized_a.append(chars)

        common_chars = []
        for c in ascii_lowercase:
            count = maxsize

            for a in characterized_a:
                if c in a:
                    count = min(count, a[c])
                else:
                    count = 0
                    break

            if count > 0:
                common_chars += [c] * count

        return common_chars


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        A = ["bella", "label", "roller"]
        # Output
        output = ["e", "l", "l"]

        solution = Solution()
        self.assertEqual(solution.commonChars(A), output)

    def test_example2(self):
        # Input
        A = ["cool", "lock", "cook"]
        # Output
        output = ["c", "o"]

        solution = Solution()
        self.assertEqual(solution.commonChars(A), output)


if __name__ == "__main__":
    unittest.main()
