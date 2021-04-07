"""
    File: 1550.py
    Title: Three Consecutive Odds
    Difficulty: Easy
    URL: https://leetcode.com/problems/three-consecutive-odds/
"""

import unittest

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        one = (arr[0] % 2) == 1
        two = (arr[1] % 2) == 1
        three = (arr[2] % 2) == 1
        if one and two and three:
            return True

        for i in range(3, len(arr)):
            one = two
            two = three
            three = (arr[i] % 2) == 1
            if one and two and three:
                return True

        return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        arr = [2, 6, 4, 1]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.threeConsecutiveOdds(arr), output)

    def test_example2(self):
        # Input
        arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.threeConsecutiveOdds(arr), output)


if __name__ == "__main__":
    unittest.main()
