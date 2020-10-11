"""
    File: 1514.py
    Title: Path with Maximum Probability
    Difficulty: Medium
    URL: https://leetcode.com/problems/path-with-maximum-probability/
"""

import heapq
import unittest

from collections import defaultdict, deque
from typing import List


class Solution:
    def maxProbability(self,
                       n: int,
                       edges: List[List[int]],
                       probs: List[float],
                       start: int,
                       end: int) -> float:
        adjacents = defaultdict(dict)
        for edge, prob in zip(edges, probs):
            a, b = edge
            adjacents[a][b] = prob
            adjacents[b][a] = prob

        heap = [(-1, start)]
        visited = [False] * n
        while heap:
            neg_prob, here = heapq.heappop(heap)

            if visited[here]:
                continue

            if here == end:
                return -neg_prob

            visited[here] = True

            for there in adjacents[here]:
                if not visited[there]:
                    there_prob = neg_prob * adjacents[here][there]
                    heapq.heappush(heap, (there_prob, there))

        return 0.0


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        probs = [0.5, 0.5, 0.2]
        start = 0
        end = 2
        # Output
        output = 0.25000

        solution = Solution()
        self.assertEqual(solution.maxProbability(n, edges, probs, start, end),
                         output)

    def test_example2(self):
        # Input
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        probs = [0.5, 0.5, 0.3]
        start = 0
        end = 2
        # Output
        output = 0.30000

        solution = Solution()
        self.assertEqual(solution.maxProbability(n, edges, probs, start, end),
                         output)

    def test_example3(self):
        # Input
        n = 3
        edges = [[0, 1]]
        probs = [0.5]
        start = 0
        end = 2
        # Output
        output = 0.00000

        solution = Solution()
        self.assertEqual(solution.maxProbability(n, edges, probs, start, end),
                         output)


if __name__ == "__main__":
    unittest.main()
