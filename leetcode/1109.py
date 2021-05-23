"""
    File: 1109.py
    Title: Corporate Flight Bookings
    Difficulty: Medium
    URL: https://leetcode.com/problems/corporate-flight-bookings/
"""

import unittest

from collections import defaultdict
from typing import List


class Solution:
    def corpFlightBookings(self,
                           bookings: List[List[int]],
                           n: int) -> List[int]:
        flights = defaultdict(int)
        for [first, last, seats] in bookings:
            flights[first - 1] += seats
            flights[last] -= seats

        ans = [0] * n
        ans[0] = flights[0]
        for flight in range(1, n):
            ans[flight] = ans[flight - 1] + flights[flight]
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
        n = 5
        # Output
        output = [10, 55, 45, 25, 25]

        solution = Solution()
        self.assertEqual(solution.corpFlightBookings(bookings, n), output)

    def test_example2(self):
        # Input
        bookings = [[1, 2, 10], [2, 2, 15]]
        n = 2
        # Output
        output = [10, 25]

        solution = Solution()
        self.assertEqual(solution.corpFlightBookings(bookings, n), output)


if __name__ == "__main__":
    unittest.main()
