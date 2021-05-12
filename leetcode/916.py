"""
    File: 916.py
    Title: Word Subsets
    Difficulty: Medium
    URL: https://leetcode.com/problems/word-subsets/
"""

import unittest

from collections import defaultdict
from typing import Dict, List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def dump(word: str) -> Dict[str, int]:
            d = defaultdict(int)
            for c in word:
                d[c] += 1
            return d

        word2_dump = defaultdict(int)
        for word in words2:
            word_dump = dump(word)
            for c in word_dump:
                word2_dump[c] = max(word2_dump[c], word_dump[c])

        ans = []
        for word in words1:
            word_dump = dump(word)

            universal = True
            for c in word2_dump:
                if word_dump[c] < word2_dump[c]:
                    universal = False
                    break
            if universal:
                ans.append(word)
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["e", "o"]
        # Output
        output = ["facebook", "google", "leetcode"]

        solution = Solution()
        self.assertEqual(solution.wordSubsets(words1, words2), output)

    def test_example2(self):
        # Input
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["l", "e"]
        # Output
        output = ["apple", "google", "leetcode"]

        solution = Solution()
        self.assertEqual(solution.wordSubsets(words1, words2), output)

    def test_example3(self):
        # Input
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["e", "oo"]
        # Output
        output = ["facebook", "google"]

        solution = Solution()
        self.assertEqual(solution.wordSubsets(words1, words2), output)

    def test_example4(self):
        # Input
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["lo", "eo"]
        # Output
        output = ["google", "leetcode"]

        solution = Solution()
        self.assertEqual(solution.wordSubsets(words1, words2), output)

    def test_example5(self):
        # Input
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["ec", "oc", "ceo"]
        # Output
        output = ["facebook", "leetcode"]

        solution = Solution()
        self.assertEqual(solution.wordSubsets(words1, words2), output)


if __name__ == "__main__":
    unittest.main()
