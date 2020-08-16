"""
    File: 299.py
    Title: Bulls and Cows
    Difficulty: Easy
    URL: https://leetcode.com/problems/bulls-and-cows/
"""

import unittest


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        s = {}
        g = {}
        for i, (a, b) in enumerate(zip(secret, guess)):
            if a == b:
                bulls += 1
            else:
                if a not in s:
                    s[a] = 0
                if b not in g:
                    g[b] = 0
                s[a] += 1
                g[b] += 1

        for k in g:
            if k in s:
                cows += min(g[k], s[k])

        return "{}A{}B".format(bulls, cows)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        secret = "1807"
        guess = "7810"
        # Output
        output = "1A3B"

        solution = Solution()
        self.assertEqual(solution.getHint(secret, guess), output)

    def test_example1(self):
        # Input
        secret = "1123"
        guess = "0111"
        # Output
        output = "1A1B"

        solution = Solution()
        self.assertEqual(solution.getHint(secret, guess), output)


if __name__ == "__main__":
    unittest.main()
