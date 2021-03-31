"""
    File: 454.py
    Title: 4Sum II
    Difficulty: Medium
    URL: https://leetcode.com/problems/4sum-ii/
"""

import unittest

from typing import List


class Solution:
    def fourSumCount(self,
                     A: List[int],
                     B: List[int],
                     C: List[int],
                     D: List[int]) -> int:
        if not A:
            return 0

        memo = {}

        for a in A:
            for b in B:
                ab = a + b
                if ab not in memo:
                    memo[ab] = 1
                else:
                    memo[ab] += 1

        count = 0
        for c in C:
            for d in D:
                cd = -(c + d)
                if cd in memo:
                    count += memo[cd]
        return count


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        A = [1, 2]
        B = [-2, -1]
        C = [-1, 2]
        D = [0, 2]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.fourSumCount(A, B, C, D), output)


if __name__ == "__main__":
    unittest.main()
