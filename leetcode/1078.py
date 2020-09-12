"""
    File: 1078.py
    Title: Occurrences After Bigram
    Difficulty: Easy
    URL: https://leetcode.com/problems/occurrences-after-bigram/
"""

import unittest

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        answer = []
        words = text.split()
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                answer.append(words[i + 2])
        return answer


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        text = "alice is a good girl she is a good student"
        first = "a"
        second = "good"
        # Output
        output = ["girl", "student"]

        solution = Solution()
        self.assertEqual(solution.findOcurrences(text, first, second), output)

    def test_example2(self):
        # Input
        text = "we will we will rock you"
        first = "we"
        second = "will"
        # Output
        output = ["we", "rock"]

        solution = Solution()
        self.assertEqual(solution.findOcurrences(text, first, second), output)


if __name__ == "__main__":
    unittest.main()
