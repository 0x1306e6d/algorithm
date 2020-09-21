"""
    File: 279.py
    Title: Perfect Squares
    Difficulty: Medium
    URL: https://leetcode.com/problems/perfect-squares/
"""

import unittest


class Solution:
    def __init__(self):
        self.squares = []
        self.cache = {}

    def numSquares(self, n: int) -> int:
        self.init_squares(n)
        return self.least_num_squares(n)

    def init_squares(self, n: int):
        for i in range(1, n):
            square = i * i
            if square > n:
                break
            self.squares.append(square)
        self.squares = list(reversed(self.squares))

    def least_num_squares(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]

        num_squares = n
        for square in self.squares:
            if n >= square:
                num_squares = min(num_squares,
                                  1 + self.least_num_squares(n - square))
        self.cache[n] = num_squares
        return num_squares


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 12
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.numSquares(n), output)

    def test_example2(self):
        # Input
        n = 13
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.numSquares(n), output)


if __name__ == "__main__":
    unittest.main()
