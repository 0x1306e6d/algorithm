"""
    File: 1232.py
    Title: Check If It Is a Straight Line
    Difficulty: Easy
    URL: https://leetcode.com/problems/check-if-it-is-a-straight-line/
"""

import unittest

from math import gcd
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        length = len(coordinates)

        gradient = None
        for i in range(length):
            x1, y1 = coordinates[i]
            for j in range(i + 1, length):
                x2, y2 = coordinates[j]

                gx, gy = self.gradient_of(x1, y1, x2, y2)
                if gradient is None:
                    gradient = (gx, gy)
                else:
                    if (gx, gy) != gradient:
                        return False
        return True

    def gradient_of(self, x1: int, y1: int, x2: int, y2: int) -> [int, int]:
        if x1 > x2:
            return self.gradient_of(x2, y2, x1, y1)
        if x1 == 0 and x2 == 0:
            return 0, 0
        if y1 == 0 and y2 == 0:
            return 0, 0
        dx = x2 - x1
        dy = y2 - y1
        g = gcd(dx, dy)
        return (dx // g), (dy // g)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.checkStraightLine(coordinates), output)

    def test_example2(self):
        # Input
        coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.checkStraightLine(coordinates), output)


if __name__ == "__main__":
    unittest.main()
