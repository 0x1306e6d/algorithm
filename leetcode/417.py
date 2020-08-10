"""
    File: 417.py
    Title: Pacific Atlantic Water Flow
    Difficulty: Medium
    URL: https://leetcode.com/problems/pacific-atlantic-water-flow/
"""

import queue
import unittest

from typing import Any, List

import queue


class Solution:

    __dx__ = [0, 0, -1, 1]
    __dy__ = [-1, 1, 0, 0]

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        pacific = set()
        pacific_visited = [[False] * n for _ in range(m)]

        pacific_q = queue.deque()
        for i in range(m):
            pacific_q.append((i, 0))
        for i in range(n):
            pacific_q.append((0, i))
        while pacific_q:
            p = pacific_q.popleft()
            pacific.add(p)

            for (dx, dy) in zip(self.__dx__, self.__dy__):
                x = p[0] + dx
                y = p[1] + dy

                if (0 <= x < m) and (0 <= y < n):
                    if pacific_visited[x][y]:
                        continue
                    if matrix[x][y] >= matrix[p[0]][p[1]]:
                        pacific_visited[x][y] = True
                        pacific_q.append((x, y))

        atlantic = set()
        atlantic_visited = [[False] * n for _ in range(m)]

        atlantic_q = queue.deque()
        for i in range(m):
            atlantic_q.append((i, n - 1))
        for i in range(n):
            atlantic_q.append((m - 1, i))
        while atlantic_q:
            p = atlantic_q.popleft()
            atlantic.add(p)

            for (dx, dy) in zip(self.__dx__, self.__dy__):
                x = p[0] + dx
                y = p[1] + dy

                if (0 <= x < m) and (0 <= y < n):
                    if atlantic_visited[x][y]:
                        continue
                    if matrix[x][y] >= matrix[p[0]][p[1]]:
                        atlantic_visited[x][y] = True
                        atlantic_q.append((x, y))

        return list(map(lambda p: [p[0], p[1]], pacific.intersection(atlantic)))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        matrix = [[1, 2, 2, 3, 5],
                  [3, 2, 3, 4, 4],
                  [2, 4, 5, 3, 1],
                  [6, 7, 1, 4, 5],
                  [5, 1, 1, 2, 4]]
        # Output
        output = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

        solution = Solution()
        self.assertListEqualInAnyOrder(solution.pacificAtlantic(matrix),
                                       output)

    def test_example2(self):
        # Input
        matrix = []
        # Output
        output = []

        solution = Solution()
        self.assertListEqualInAnyOrder(solution.pacificAtlantic(matrix),
                                       output)

    def assertListEqualInAnyOrder(self, a: List[Any], b: List[Any]) -> bool:
        if len(a) != len(b):
            self.fail()

        for p in a:
            if p not in b:
                self.fail()


if __name__ == "__main__":
    unittest.main()
