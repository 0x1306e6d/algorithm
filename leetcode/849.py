"""
    File: 849.py
    Title: Maximize Distance to Closest Person
    Difficulty: Medium
    URL: https://leetcode.com/problems/maximize-distance-to-closest-person/
"""

import unittest

from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first_seat = self.lfind(seats)
        last_seat = self.rfind(seats)

        max_distance = max(first_seat, len(seats) - last_seat - 1)
        if first_seat == last_seat:
            return max_distance

        before = first_seat
        for i in range(first_seat + 1, last_seat + 1):
            if seats[i] == 1:
                max_distance = max(max_distance, (i - before) // 2)
                before = i
        return max_distance

    def lfind(self, seats: List[int]) -> int:
        return seats.index(1)

    def rfind(self, seats: List[int]) -> int:
        for i, seat in enumerate(reversed(seats)):
            if seat == 1:
                return len(seats) - i - 1


class SolutionTestCase(unittest.TestCase):
    # 1 0 0 1
    def test_example1(self):
        # Input
        seats = [1, 0, 0, 0, 1, 0, 1]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.maxDistToClosest(seats), output)

    def test_example2(self):
        # Input
        seats = [1, 0, 0, 0]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.maxDistToClosest(seats), output)

    def test_example3(self):
        # Input
        seats = [0, 1]
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.maxDistToClosest(seats), output)


if __name__ == "__main__":
    unittest.main()
