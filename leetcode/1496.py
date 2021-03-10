"""
    File: 1496.py
    Title: Path Crossing
    Difficulty: Easy
    URL: https://leetcode.com/problems/path-crossing/
"""

import unittest

MAX_LENGTH = 1001


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        plane = [[False] * (MAX_LENGTH * 2) for _ in range(MAX_LENGTH * 2)]

        x = 0
        y = 0
        plane[y][x] = True
        for walk in path:
            if walk == 'N':
                y += 1
            elif walk == 'S':
                y -= 1
            elif walk == 'E':
                x += 1
            else:
                x -= 1

            if plane[y][x]:
                return True
            plane[y][x] = True

        return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        path = "NES"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isPathCrossing(path), output)

    def test_example2(self):
        # Input
        path = "NESWW"
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isPathCrossing(path), output)


if __name__ == "__main__":
    unittest.main()
