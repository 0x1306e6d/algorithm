"""
    File: 204.py
    Title: Count Primes
    Difficulty: Easy
    URL: https://leetcode.com/problems/count-primes/
"""

import unittest

from math import sqrt
from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        sieve = [True] * n
        sieve[0] = False
        sieve[1] = False
        for i in range(2, int(sqrt(n)) + 1):
            if sieve[i]:
                for j in range(i * i, n, i):
                    sieve[j] = False
        return sieve.count(True)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 10
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.countPrimes(n), output)

    def test_example2(self):
        # Input
        n = 0
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.countPrimes(n), output)

    def test_example3(self):
        # Input
        n = 1
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.countPrimes(n), output)


if __name__ == "__main__":
    unittest.main()
