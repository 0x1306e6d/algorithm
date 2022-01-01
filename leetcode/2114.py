"""
    File: 2114.py
    Title: Maximum Number of Words Found in Sentences
    Difficulty: Easy
    URL: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
"""

import unittest

from functools import reduce
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        word_counts = list(map(lambda s: s.count(" ") + 1, sentences))
        return reduce(lambda acc, cur: max(acc, cur), word_counts, 0)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        sentences = ["alice and bob love leetcode",
                     "i think so too",
                     "this is great thanks very much"]
        # Output
        output = 6

        solution = Solution()
        self.assertEqual(solution.mostWordsFound(sentences), output)

    def test_example2(self):
        # Input
        sentences = ["please wait", "continue to fight", "continue to win"]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.mostWordsFound(sentences), output)


if __name__ == "__main__":
    unittest.main()
