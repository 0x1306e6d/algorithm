"""
    File: 1184.py
    Title: Distance Between Bus Stops
    Difficulty: Easy
    URL: https://leetcode.com/problems/distance-between-bus-stops/
"""

import unittest

from typing import List


class Solution:
    def distanceBetweenBusStops(self,
                                distance: List[int],
                                start: int,
                                destination: int) -> int:
        if start > destination:
            return self.distanceBetweenBusStops(distance, destination, start)

        distance_between = 0
        for i in range(start, destination):
            distance_between += distance[i]

        distance_outer = 0
        for i in range(start):
            distance_outer += distance[i]
        for i in range(destination, len(distance)):
            distance_outer += distance[i]

        return min(distance_between, distance_outer)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        distance = [1, 2, 3, 4]
        start = 0
        destination = 1
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.distanceBetweenBusStops(distance,
                                                          start,
                                                          destination),
                         output)

    def test_example2(self):
        # Input
        distance = [1, 2, 3, 4]
        start = 0
        destination = 2
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.distanceBetweenBusStops(distance,
                                                          start,
                                                          destination),
                         output)

    def test_example3(self):
        # Input
        distance = [1, 2, 3, 4]
        start = 0
        destination = 3
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.distanceBetweenBusStops(distance,
                                                          start,
                                                          destination),
                         output)


if __name__ == "__main__":
    unittest.main()
