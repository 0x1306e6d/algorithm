"""
    File: 746.py
    Title: Min Cost Climbing Stairs
    Difficulty: Easy
    URL: https://leetcode.com/problems/min-cost-climbing-stairs/
"""

import unittest

from typing import List


class Solution:
    def __init__(self):
        self.costs = []
        self.dp = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.costs = cost

        return min(self.min_cost(0), self.min_cost(1))

    def min_cost(self, i: int):
        if i in self.dp:
            return self.dp[i]

        if i >= len(self.costs):
            return 0

        cost = min(self.min_cost(i + 1), self.min_cost(i + 2)) + self.costs[i]
        self.dp[i] = cost
        return cost


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        cost = [10, 15, 20]
        # Output
        output = 15

        solution = Solution()
        self.assertEqual(solution.minCostClimbingStairs(cost), output)

    def test_example2(self):
        # Input
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        # Output
        output = 6

        solution = Solution()
        self.assertEqual(solution.minCostClimbingStairs(cost), output)


if __name__ == "__main__":
    unittest.main()
