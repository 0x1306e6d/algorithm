"""
    File: 1222.py
    Title: Queens That Can Attack the King
    Difficulty: Medium
    URL: https://leetcode.com/problems/queens-that-can-attack-the-king/
"""

import unittest

from typing import Any, List


class Solution:

    __dx__ = [0, 1, 1, 1, 0, -1, -1, -1]
    __dy__ = [-1, -1, 0, 1, 1, 1, 0, -1]

    def queensAttacktheKing(self,
                            queens: List[List[int]],
                            king: List[int]) -> List[List[int]]:
        chessboard = [[False] * 8 for _ in range(8)]
        for queen in queens:
            chessboard[queen[1]][queen[0]] = True

        can_attack = [None] * 8
        for i in range(1, 8):
            for j, (dx, dy) in enumerate(zip(self.__dx__, self.__dy__)):
                if can_attack[j] is not None:
                    continue

                x = king[0] + (dx * i)
                y = king[1] + (dy * i)
                if (0 <= x < 8) and (0 <= y < 8):
                    if chessboard[y][x]:
                        can_attack[j] = [x, y]

        return list(filter(lambda it: it is not None, can_attack))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
        king = [0, 0]
        # Output
        output = [[0, 1], [1, 0], [3, 3]]

        solution = Solution()
        self.assertListEqualInAnyOrder(
            solution.queensAttacktheKing(queens, king), output)

    def test_example2(self):
        # Input
        queens = [[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]]
        king = [3, 3]
        # Output
        output = [[2, 2], [3, 4], [4, 4]]

        solution = Solution()
        self.assertListEqualInAnyOrder(
            solution.queensAttacktheKing(queens, king), output)

    def test_example3(self):
        # Input
        queens = [[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7],
                  [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4], [2, 2],
                  [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2],
                  [1, 4], [7, 5], [2, 3], [0, 5], [4, 2], [1, 0], [2, 7],
                  [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]]
        king = [3, 4]
        # Output
        output = [[2, 3], [1, 4], [1, 6], [3, 7], [4, 3], [5, 4], [4, 5]]

        solution = Solution()
        self.assertListEqualInAnyOrder(
            solution.queensAttacktheKing(queens, king), output)

    def assertListEqualInAnyOrder(self, a: List[Any], b: List[Any]) -> bool:
        if len(a) != len(b):
            self.fail()

        for p in a:
            if p not in b:
                self.fail()


if __name__ == "__main__":
    unittest.main()
