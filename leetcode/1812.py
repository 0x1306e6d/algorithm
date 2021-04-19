"""
    File: 1812.py
    Title: Determine Color of a Chessboard Square
    Difficulty: Easy
    URL: https://leetcode.com/problems/determine-color-of-a-chessboard-square/
"""

import unittest


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0]) - ord('a') + 1
        y = int(coordinates[1])
        return ((x + y) % 2) == 1


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        coordinates = "a1"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.squareIsWhite(coordinates), output)

    def test_example2(self):
        # Input
        coordinates = "h3"
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.squareIsWhite(coordinates), output)

    def test_example3(self):
        # Input
        coordinates = "c7"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.squareIsWhite(coordinates), output)


if __name__ == "__main__":
    unittest.main()
