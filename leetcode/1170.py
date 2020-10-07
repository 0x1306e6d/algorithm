"""
    File: 1170.py
    Title: Compare Strings by Frequency of the Smallest Character
    Difficulty: Easy
    URL: https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
"""

import unittest

from typing import List


class Solution:
    def numSmallerByFrequency(self,
                              queries: List[str],
                              words: List[str]) -> List[int]:
        f_queries = [self.f(query) for query in queries]
        f_words = [self.f(word) for word in words]
        return [self.lt(f_query, f_words) for f_query in f_queries]

    def f(self, s: str) -> int:
        return s.count(min(s))

    def lt(self, i: int, arr: List[int]) -> int:
        count = 0
        for j in arr:
            if i < j:
                count += 1
        return count


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        queries = ["cbd"]
        words = ["zaaaz"]
        # Output
        output = [1]

        solution = Solution()
        self.assertEqual(solution.numSmallerByFrequency(queries, words),
                         output)

    def test_example2(self):
        # Input
        queries = ["bbb", "cc"]
        words = ["a", "aa", "aaa", "aaaa"]
        # Output
        output = [1, 2]

        solution = Solution()
        self.assertEqual(solution.numSmallerByFrequency(queries, words),
                         output)


if __name__ == "__main__":
    unittest.main()
