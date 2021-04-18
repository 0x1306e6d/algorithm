"""
    File: 1094.py
    Title: Car Pooling
    Difficulty: Medium
    URL: https://leetcode.com/problems/car-pooling/
"""

import heapq
import unittest

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(map(lambda trip: ((trip[1], trip[2]), trip[0]), trips))

        vehicle = 0
        pq = []
        for trip in trips:
            (start, end), passengers = trip

            while pq and pq[0][0] <= start:
                vehicle -= pq[0][1]
                heapq.heappop(pq)

            if vehicle + passengers > capacity:
                return False
            vehicle += passengers

            heapq.heappush(pq, (end, passengers))

        return True


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 4
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.carPooling(trips, capacity), output)

    def test_example2(self):
        # Input
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 5
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.carPooling(trips, capacity), output)

    def test_example3(self):
        # Input
        trips = [[2, 1, 5], [3, 5, 7]]
        capacity = 3
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.carPooling(trips, capacity), output)

    def test_example4(self):
        # Input
        trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
        capacity = 11
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.carPooling(trips, capacity), output)


if __name__ == "__main__":
    unittest.main()
