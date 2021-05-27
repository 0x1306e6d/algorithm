"""
    File: 139.py
    Title: Word Break
    Difficulty: Medium
    URL: https://leetcode.com/problems/word-break/
"""

import unittest

from typing import List


class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        trie = {}
        for word in words:
            current = trie
            for c in word:
                if c not in current:
                    current[c] = {}
                current = current[c]
            current[0] = True

        memo = {}

        def find(i: int) -> bool:
            if i in memo:
                return memo[i]

            current = trie
            for j in range(i, len(s)):
                c = s[j]
                if c in current:
                    current = current[c]
                    if 0 in current:
                        if find(j + 1):
                            memo[i] = True
                            return True
                else:
                    memo[i] = False
                    return False
            memo[i] = (0 in current)
            return memo[i]

        return find(0)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "leetcode"
        words = ["leet", "code"]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.wordBreak(s, words), output)

    def test_example2(self):
        # Input
        s = "applepenapple"
        words = ["apple", "pen"]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.wordBreak(s, words), output)

    def test_example3(self):
        # Input
        s = "catsandog"
        words = ["cats", "dog", "sand", "and", "cat"]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.wordBreak(s, words), output)

    def test_example4(self):
        # Input
        s = "aaaaaaa"
        words = ["aaaa", "aa"]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.wordBreak(s, words), output)


if __name__ == "__main__":
    unittest.main()
