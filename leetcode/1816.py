"""
    File: 1816.py
    Title: Truncate Sentence
    Difficulty: Easy
    URL: https://leetcode.com/problems/truncate-sentence/
"""

import unittest


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "Hello how are you Contestant"
        k = 4
        # Output
        output = "Hello how are you"

        solution = Solution()
        self.assertEqual(solution.truncateSentence(s, k), output)

    def test_example2(self):
        # Input
        s = "What is the solution to this problem"
        k = 4
        # Output
        output = "What is the solution"

        solution = Solution()
        self.assertEqual(solution.truncateSentence(s, k), output)

    def test_example3(self):
        # Input
        s = "chopper is not a tanuki"
        k = 5
        # Output
        output = "chopper is not a tanuki"

        solution = Solution()
        self.assertEqual(solution.truncateSentence(s, k), output)


if __name__ == "__main__":
    unittest.main()
