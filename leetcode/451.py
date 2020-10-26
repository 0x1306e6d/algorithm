"""
    File: 451.py
    Title: Sort Characters By Frequency
    Difficulty: Medium
    URL: https://leetcode.com/problems/sort-characters-by-frequency/
"""

import unittest


class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        trie = {}
        for i, c in enumerate(s):
            if c in trie:
                t = trie[c]
                trie[c] = (t[0] + 1, t[1], t[2])
            else:
                trie[c] = (1, n - i, c)

        fsort = ""
        for t in reversed(sorted(trie.values())):
            fsort += (t[2] * t[0])
        return fsort


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "tree"
        # Output
        output = "eetr"

        solution = Solution()
        self.assertEqual(solution.frequencySort(s), output)

    def test_example2(self):
        # Input
        s = "cccaaa"
        # Output
        output = "cccaaa"

        solution = Solution()
        self.assertEqual(solution.frequencySort(s), output)

    def test_example3(self):
        # Input
        s = "Aabb"
        # Output
        output = "bbAa"

        solution = Solution()
        self.assertEqual(solution.frequencySort(s), output)


if __name__ == "__main__":
    unittest.main()
