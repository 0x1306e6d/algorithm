"""
    File: 207.py
    Title: Course Schedule
    Difficulty: Medium
    URL: https://leetcode.com/problems/course-schedule/
"""

import unittest

from collections import defaultdict
from queue import deque
from typing import List


class Solution:
    def canFinish(self,
                  num_courses: int,
                  prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        adjacents = defaultdict(list)
        for a, b in prerequisites:
            indegree[b] += 1
            adjacents[a].append(b)

        q = deque()
        for i in range(num_courses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            here = q.popleft()

            for there in adjacents[here]:
                indegree[there] -= 1
                if indegree[there] == 0:
                    q.append(there)
        return all(val == 0 for val in indegree.values())


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        num_courses = 2
        prerequisites = [[1, 0]]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.canFinish(num_courses, prerequisites),
                         output)

    def test_example2(self):
        # Input
        num_courses = 2
        prerequisites = [[1, 0], [0, 1]]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.canFinish(num_courses, prerequisites),
                         output)


if __name__ == "__main__":
    unittest.main()
