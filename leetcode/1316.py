"""
    File: 1316.py
    Title: Distinct Echo Substrings
    Difficulty: Hard
    URL: https://leetcode.com/problems/distinct-echo-substrings/
"""

import unittest

from collections import defaultdict


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        ans = 0
        memo = defaultdict(int)
        for i in range(len(text) + 1):
            for j in range(i + 2, len(text) + 1):
                if ((j - i) % 2) != 0:
                    continue

                mid = (i + j) // 2
                first = text[i:mid]
                second = text[mid:j]
                if first == second:
                    if memo[first] == 0:
                        ans += 1
                    memo[first] += 1
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        text = "abcabcabc"
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.distinctEchoSubstrings(text), output)

    def test_example2(self):
        # Input
        text = "leetcodeleetcode"
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.distinctEchoSubstrings(text), output)


if __name__ == "__main__":
    unittest.main()
