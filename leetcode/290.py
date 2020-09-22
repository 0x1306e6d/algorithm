"""
    File: 290.py
    Title: Word Pattern
    Difficulty: Easy
    URL: https://leetcode.com/problems/word-pattern/
"""

import unittest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = list(s.split())
        if len(pattern) != len(words):
            return False

        bijection = {}
        for c, word in zip(pattern, words):
            if c in bijection:
                if bijection[c] != word:
                    return False
            else:
                if word in bijection.values():
                    return False
                bijection[c] = word
        return True


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        pattern = "abba"
        s = "dog cat cat dog"
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern, s), output)

    def test_example2(self):
        # Input
        pattern = "abba"
        s = "dog cat cat fish"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern, s), output)

    def test_example3(self):
        # Input
        pattern = "aaaa"
        s = "dog cat cat dog"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern, s), output)

    def test_example4(self):
        # Input
        pattern = "abba"
        s = "dog dog dog dog"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern, s), output)


if __name__ == "__main__":
    unittest.main()
