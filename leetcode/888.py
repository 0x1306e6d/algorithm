"""
    File: 888.py
    Title: Fair Candy Swap
    Difficulty: Easy
    URL: https://leetcode.com/problems/fair-candy-swap/
"""

import unittest

from typing import List


class Solution:
    def fairCandySwap(self, a: List[int], b: List[int]) -> List[int]:
        a_set = set(a)
        b_set = set(b)

        d = (sum(a) - sum(b)) // 2
        for i in a_set:
            if i - d in b_set:
                return [i, i - d]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        a = [1, 1]
        b = [2, 2]
        # Output
        output = [1, 2]

        solution = Solution()
        self.assertEqual(solution.fairCandySwap(a, b), output)

    def test_example2(self):
        # Input
        a = [1, 2]
        b = [2, 3]
        # Output
        output = [1, 2]

        solution = Solution()
        self.assertEqual(solution.fairCandySwap(a, b), output)

    def test_example3(self):
        # Input
        a = [2]
        b = [1, 3]
        # Output
        output = [2, 3]

        solution = Solution()
        self.assertEqual(solution.fairCandySwap(a, b), output)

    def test_example4(self):
        # Input
        a = [1, 2, 5]
        b = [2, 4]
        # Output
        output = [5, 4]

        solution = Solution()
        self.assertEqual(solution.fairCandySwap(a, b), output)


if __name__ == "__main__":
    unittest.main()
