"""
    File: 1160.py
    Title: Find Words That Can Be Formed by Characters
    Difficulty: Easy
    URL: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
"""

import unittest

from collections import defaultdict
from typing import Dict, List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def dump(word: str) -> Dict[str, int]:
            d = defaultdict(int)
            for c in word:
                d[c] += 1
            return d

        chars_dump = dump(chars)

        ans = 0
        for word in words:
            word_dump = dump(word)

            good = True
            for c in word_dump:
                if word_dump[c] > chars_dump[c]:
                    good = False
                    break
            if good:
                print(word)
                ans += len(word)
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        words = ["cat", "bt", "hat", "tree"]
        chars = "atach"
        # Output
        output = 6

        solution = Solution()
        self.assertEqual(solution.countCharacters(words, chars), output)

    def test_example2(self):
        # Input
        words = ["hello", "world", "leetcode"]
        chars = "welldonehoneyr"
        # Output
        output = 10

        solution = Solution()
        self.assertEqual(solution.countCharacters(words, chars), output)


if __name__ == "__main__":
    unittest.main()
