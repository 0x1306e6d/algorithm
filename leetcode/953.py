"""
    File: 953.py
    Title: Verifying an Alien Dictionary
    Difficulty: Easy
    URL: https://leetcode.com/problems/verifying-an-alien-dictionary/
"""

import unittest

from functools import cmp_to_key
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compare(a: str, b: str):
            i = 0
            j = 0
            while True:
                i_order = order.find(a[i])
                j_order = order.find(b[j])

                if i_order < j_order:
                    return 1
                elif i_order > j_order:
                    return -1
                else:
                    i += 1
                    if i >= len(a):
                        return 1
                    j += 1
                    if j >= len(b):
                        return -1
        sorted_words = sorted(words, key=cmp_to_key(compare), reverse=True)
        return words == sorted_words


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isAlienSorted(words, order), output)

    def test_example2(self):
        # Input
        words = ["word", "world", "row"]
        order = "worldabcefghijkmnpqstuvxyz"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isAlienSorted(words, order), output)

    def test_example3(self):
        # Input
        words = ["apple", "app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isAlienSorted(words, order), output)

    def test_example4(self):
        # Input
        words = ["kuvp", "q"]
        order = "ngxlkthsjuoqcpavbfdermiywz"
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isAlienSorted(words, order), output)


if __name__ == "__main__":
    unittest.main()
