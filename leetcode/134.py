"""
    File: 134.py
    Title: Gas Station
    Difficulty: Medium
    URL: https://leetcode.com/problems/gas-station/
"""

import unittest

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        complete = (sum(gas) - sum(cost)) >= 0
        if not complete:
            return -1

        tank = 0
        answer = 987654321
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += (g - c)
            if tank >= 0:
                answer = min(answer, i)
            else:
                tank = 0
                answer = 987654321
        return answer


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.canCompleteCircuit(gas, cost), output)

    def test_example2(self):
        # Input
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        # Output
        output = -1

        solution = Solution()
        self.assertEqual(solution.canCompleteCircuit(gas, cost), output)


if __name__ == "__main__":
    unittest.main()
