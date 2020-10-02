"""
    File: 211.py
    Title: Design Add and Search Words Data Structure
    Difficulty: Medium
    URL: https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""

import unittest

from typing import Dict


class WordDictionary:
    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        current = self.words
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current[0] = True

    def search(self, word: str) -> bool:
        return self.do_search(word, self.words)

    def do_search(self, word: str, words: Dict[str, Dict]) -> bool:
        current = words
        for i, c in enumerate(word):
            if c == '.':
                next_word = word[i + 1:]
                for next_c in current:
                    if next_c == 0:
                        continue
                    if self.do_search(next_word, current[next_c]):
                        return True
                return False
            else:
                if c not in current:
                    return False
                current = current[c]
        return 0 in current


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        dictionary = WordDictionary()
        dictionary.addWord("bad")
        dictionary.addWord("dad")
        dictionary.addWord("mad")
        self.assertEqual(dictionary.search("pad"), False)
        self.assertEqual(dictionary.search("bad"), True)
        self.assertEqual(dictionary.search(".ad"), True)
        self.assertEqual(dictionary.search("b.."), True)


if __name__ == "__main__":
    unittest.main()
