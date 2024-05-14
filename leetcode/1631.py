"""
    File: 1631.py
    Title: Path With Minimum Effort
    Difficulty: Medium
    URL: https://leetcode.com/problems/path-with-minimum-effort/
"""

from heapq import heappush, heappop
from typing import List

__dx__ = [0, 0, -1, 1]
__dy__ = [-1, 1, 0, 0]


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        inf = 9876543210
        distance = [[inf] * cols for _ in range(rows)]

        h = [(0, 0, 0)]
        while h:
            d, x1, y1 = heappop(h)

            if distance[y1][x1] <= d:
                continue
            distance[y1][x1] = d

            for dx, dy in zip(__dx__, __dy__):
                x2, y2 = x1 + dx, y1 + dy
                if 0 <= x2 < cols and 0 <= y2 < rows:
                    w = abs(heights[y2][x2] - heights[y1][x1])
                    w = max(w, d)
                    if distance[y2][x2] > w:
                        heappush(h, (w, x2, y2))
        return distance[rows - 1][cols - 1]
