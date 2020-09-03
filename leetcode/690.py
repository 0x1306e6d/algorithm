"""
    File: 690.py
    Title: Employee Importance
    Difficulty: Easy
    URL: https://leetcode.com/problems/employee-importance/
"""

import unittest

from typing import List
from queue import deque


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], target: int) -> int:
        employees_map = {}
        for employee in employees:
            employees_map[employee.id] = employee

        importance = 0
        q = deque()
        q.append(target)
        while q:
            p = q.popleft()

            employee = employees_map[p]
            importance += employee.importance
            for subordinate in employee.subordinates:
                q.append(subordinate)
        return importance


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        # [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
        employees = [Employee(1, 5, [2, 3]),
                     Employee(2, 3, []),
                     Employee(3, 3, [])]
        target = 1
        # Output
        output = 11

        solution = Solution()
        self.assertEqual(solution.getImportance(employees, target), output)


if __name__ == "__main__":
    unittest.main()
