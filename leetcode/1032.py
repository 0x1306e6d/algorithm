"""
    File: 1032.py
    Title: Stream of Characters
    Difficulty: Hard
    URL: https://leetcode.com/problems/stream-of-characters/
"""

import unittest

from typing import List


class StreamChecker:
    def __init__(self, words: List[str]):
        self.tree = {}
        for word in words:
            current = self.tree
            for c in reversed(word):
                if c not in current:
                    current[c] = {}
                current = current[c]
            current[0] = True
        self.query_str = ""

    def query(self, letter: str) -> bool:
        self.query_str += letter

        current = self.tree
        for c in reversed(self.query_str):
            if c in current:
                current = current[c]
                if 0 in current:
                    return True
            else:
                return False
        return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        stream_checker = StreamChecker(["cd", "f", "kl"])
        self.assertFalse(stream_checker.query('a'))
        self.assertFalse(stream_checker.query('b'))
        self.assertFalse(stream_checker.query('c'))
        self.assertTrue(stream_checker.query('d'))
        self.assertFalse(stream_checker.query('e'))
        self.assertTrue(stream_checker.query('f'))
        self.assertFalse(stream_checker.query('g'))
        self.assertFalse(stream_checker.query('h'))
        self.assertFalse(stream_checker.query('i'))
        self.assertFalse(stream_checker.query('j'))
        self.assertFalse(stream_checker.query('k'))
        self.assertTrue(stream_checker.query('l'))


if __name__ == "__main__":
    unittest.main()
