"""
    File: 1535.py
    Title: Find the Winner of an Array Game
    Difficulty: Medium
    URL: https://leetcode.com/problems/find-the-winner-of-an-array-game/
"""

import unittest

from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])

        winner = max(arr[0], arr[1])
        win_count = 1
        for i in range(2, len(arr)):
            if winner > arr[i]:
                win_count += 1
                if win_count >= k:
                    return winner
            else:
                winner = arr[i]
                win_count = 1
        return max(arr)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        arr = [2, 1, 3, 5, 4, 6, 7]
        k = 2
        # Output
        output = 5

        solution = Solution()
        self.assertEqual(solution.getWinner(arr, k), output)

    def test_example2(self):
        # Input
        arr = [3, 2, 1]
        k = 10
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.getWinner(arr, k), output)

    def test_example3(self):
        # Input
        arr = [1, 9, 8, 2, 3, 7, 6, 4, 5]
        k = 7
        # Output
        output = 9

        solution = Solution()
        self.assertEqual(solution.getWinner(arr, k), output)

    def test_example4(self):
        # Input
        arr = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
        k = 1000000000
        # Output
        output = 99

        solution = Solution()
        self.assertEqual(solution.getWinner(arr, k), output)


if __name__ == "__main__":
    unittest.main()
