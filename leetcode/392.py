"""
    File: 392.py
    Title: Is Subsequence
    Difficulty: Easy
    URL: https://leetcode.com/problems/is-subsequence/
"""

import unittest

from collections import defaultdict
from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        hash_map = defaultdict(list)
        for i, c in enumerate(t):
            hash_map[c].append(i)

        index = None
        for c in s:
            if c not in hash_map:
                return False

            if index is None:
                index = hash_map[c][0]
            else:
                found = False
                for j in hash_map[c]:
                    if j > index:
                        index = j
                        found = True
                        break
                if not found:
                    return False
        return True


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "abc"
        t = "ahbgdc"
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isSubsequence(s, t), output)

    def test_example2(self):
        # Input
        s = "axc"
        t = "ahbgdc"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isSubsequence(s, t), output)


if __name__ == "__main__":
    unittest.main()
