"""
    File: 520.py
    Title: Detect Capital
    Difficulty: Easy
    URL: https://leetcode.com/problems/detect-capital/
"""

import unittest


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = 0
        for c in word:
            if 'A' <= c <= 'Z':
                capitals += 1

        if capitals == 1:
            if 'A' <= word[0] <= 'Z':
                return True
        if capitals == len(word) or capitals == 0:
            return True
        return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        word = "USA"
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.detectCapitalUse(word), output)

    def test_example1(self):
        # Input
        word = "FlaG"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.detectCapitalUse(word), output)


if __name__ == "__main__":
    unittest.main()
