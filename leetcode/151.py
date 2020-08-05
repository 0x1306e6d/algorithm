"""
    File: 151.py
    Title: Reverse Words in a String
    Difficulty: Medium
    URL: https://leetcode.com/problems/reverse-words-in-a-string/
"""

import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return ' '.join(reversed(words))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "the sky is blue"
        # Output
        output = "blue is sky the"

        solution = Solution()
        self.assertEqual(solution.reverseWords(s), output)

    def test_example2(self):
        # Input
        s = "  hello world!  "
        # Output
        output = "world! hello"

        solution = Solution()
        self.assertEqual(solution.reverseWords(s), output)

    def test_example3(self):
        # Input
        s = "a good   example"
        # Output
        output = "example good a"

        solution = Solution()
        self.assertEqual(solution.reverseWords(s), output)


if __name__ == "__main__":
    unittest.main()
