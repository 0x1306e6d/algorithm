"""
    File: 1376.py
    Title: Time Needed to Inform All Employees
    Difficulty: Medium
    URL: https://leetcode.com/problems/time-needed-to-inform-all-employees/
"""

import unittest

from collections import deque
from typing import List


class Solution:
    def numOfMinutes(self,
                     n: int,
                     head_id: int,
                     manager: List[int],
                     inform_time: List[int]) -> int:
        max_inform_time = 0

        graph = {}
        for i in range(n):
            graph[i] = []

        for i, m in enumerate(manager):
            if m == -1:
                continue
            graph[m].append(i)

        q = deque()
        q.append((head_id, 0))
        while q:
            employee, current_inform_time = q.pop()

            next_inform_time = current_inform_time + inform_time[employee]
            max_inform_time = max(max_inform_time, next_inform_time)

            for subordinate in graph[employee]:
                q.append((subordinate, next_inform_time))
        return max_inform_time


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 1
        head_id = 0
        manager = [-1]
        inform_time = [0]
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.numOfMinutes(n,
                                               head_id,
                                               manager,
                                               inform_time),
                         output)

    def test_example2(self):
        # Input
        n = 6
        head_id = 2
        manager = [2, 2, -1, 2, 2, 2]
        inform_time = [0, 0, 1, 0, 0, 0]
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.numOfMinutes(n,
                                               head_id,
                                               manager,
                                               inform_time),
                         output)

    def test_example3(self):
        # Input
        n = 7
        head_id = 6
        manager = [1, 2, 3, 4, 5, 6, -1]
        inform_time = [0, 6, 5, 4, 3, 2, 1]
        # Output
        output = 21

        solution = Solution()
        self.assertEqual(solution.numOfMinutes(n,
                                               head_id,
                                               manager,
                                               inform_time),
                         output)

    def test_example4(self):
        # Input
        n = 15
        head_id = 0
        manager = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
        inform_time = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.numOfMinutes(n,
                                               head_id,
                                               manager,
                                               inform_time),
                         output)

    def test_example5(self):
        # Input
        n = 4
        head_id = 2
        manager = [3, 3, -1, 2]
        inform_time = [0, 0, 162, 914]
        # Output
        output = 1076

        solution = Solution()
        self.assertEqual(solution.numOfMinutes(n,
                                               head_id,
                                               manager,
                                               inform_time),
                         output)


if __name__ == "__main__":
    unittest.main()
