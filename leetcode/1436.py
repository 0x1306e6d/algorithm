"""
    File: 1436.py
    Title: Destination City
    Difficulty: Easy
    URL: https://leetcode.com/problems/destination-city/
"""

import unittest

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = {}
        for a, b in paths:
            cities[a] = True
            if b not in cities:
                cities[b] = False
        for city in cities:
            if not cities[city]:
                return city


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        paths = [["London", "New York"],
                 ["New York", "Lima"],
                 ["Lima", "Sao Paulo"]]
        # Output
        output = "Sao Paulo"

        solution = Solution()
        self.assertEqual(solution.destCity(paths), output)

    def test_example2(self):
        # Input
        paths = [["B", "C"], ["D", "B"], ["C", "A"]]
        # Output
        output = "A"

        solution = Solution()
        self.assertEqual(solution.destCity(paths), output)

    def test_example3(self):
        # Input
        paths = [["A", "Z"]]
        # Output
        output = "Z"

        solution = Solution()
        self.assertEqual(solution.destCity(paths), output)


if __name__ == "__main__":
    unittest.main()
