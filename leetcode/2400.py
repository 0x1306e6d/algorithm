"""
    File: 2400.py
    Title: Number of Ways to Reach a Position After Exactly k Steps
    Difficulty: Medium
"""

import unittest

from math import comb

MOD = pow(10, 9) + 7


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        distance = abs(endPos - startPos)
        if distance > k:
            return 0
        if distance == k:
            return 1
        if (k - distance) % 2 == 1:
            return 0
        move = (k - distance) // 2
        return comb(k, move) % MOD


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        startPos = 1
        endPos = 2
        k = 3
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.numberOfWays(startPos, endPos, k), output)

    def test_example2(self):
        # Input
        startPos = 2
        endPos = 5
        k = 10
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.numberOfWays(startPos, endPos, k), output)


if __name__ == "__main__":
    unittest.main()
