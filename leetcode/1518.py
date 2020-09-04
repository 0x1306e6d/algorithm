"""
    File: 1518.py
    Title: Water Bottles
    Difficulty: Easy
    URL: https://leetcode.com/problems/water-bottles/
"""

import unittest


class Solution:
    def numWaterBottles(self, num_bottles: int, num_exchange: int) -> int:
        maximum = 0

        full = num_bottles
        empty = 0
        while full:
            maximum += full
            empty += full

            full = empty // num_exchange
            empty %= num_exchange

        return maximum


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        num_bottles = 9
        num_exchange = 3
        # Output
        output = 13

        solution = Solution()
        self.assertEqual(solution.numWaterBottles(num_bottles, num_exchange),
                         output)

    def test_example2(self):
        # Input
        num_bottles = 15
        num_exchange = 4
        # Output
        output = 19

        solution = Solution()
        self.assertEqual(solution.numWaterBottles(num_bottles, num_exchange),
                         output)

    def test_example3(self):
        # Input
        num_bottles = 5
        num_exchange = 5
        # Output
        output = 6

        solution = Solution()
        self.assertEqual(solution.numWaterBottles(num_bottles, num_exchange),
                         output)

    def test_example4(self):
        # Input
        num_bottles = 2
        num_exchange = 3
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.numWaterBottles(num_bottles, num_exchange),
                         output)


if __name__ == "__main__":
    unittest.main()
