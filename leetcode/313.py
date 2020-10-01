"""
    File: 313.py
    Title: Super Ugly Number
    Difficulty: Medium
    URL: https://leetcode.com/problems/super-ugly-number/
"""

import heapq
import unittest

from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1

        ugly_number = 1
        heap = [(prime, i) for i, prime in enumerate(sorted(primes))]
        for i in range(n - 1):
            ugly_number, here = heapq.heappop(heap)
            for there in range(here, len(primes)):
                heapq.heappush(heap, (ugly_number * primes[there], there))
        return ugly_number


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 12
        primes = [2, 7, 13, 19]
        # Output
        output = 32

        solution = Solution()
        self.assertEqual(solution.nthSuperUglyNumber(n, primes), output)


if __name__ == "__main__":
    unittest.main()
