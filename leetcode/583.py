"""
    File: 583.py
    Title: Delete Operation for Two Strings
    Difficulty: Medium
    URL: https://leetcode.com/problems/delete-operation-for-two-strings/
"""

import unittest


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def lcs(i: int, j: int) -> int:
            if (i == len(word1)) or (j == len(word2)):
                return 0

            if i not in memo:
                memo[i] = {}
            if j in memo[i]:
                return memo[i][j]

            if word1[i] == word2[j]:
                memo[i][j] = 1 + lcs(i + 1, j + 1)
            else:
                memo[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))
            return memo[i][j]

        to_delete = lcs(0, 0)
        return (len(word1) - to_delete) + (len(word2) - to_delete)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        word1 = "sea"
        word2 = "eat"
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.minDistance(word1, word2), output)

    def test_example2(self):
        # Input
        word1 = "leetcode"
        word2 = "etco"
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.minDistance(word1, word2), output)


if __name__ == "__main__":
    unittest.main()
