"""
    File: 1584.py
    Title: Min Cost to Connect All Points
    Difficulty: Medium
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        h = []
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                d = abs(x1 - x2) + abs(y1 - y2)
                heappush(h, (d, (x1, y1), (x2, y2)))

        uf = {}

        def find(i):
            if i not in uf:
                uf[i] = i
            if i == uf[i]:
                return i
            uf[i] = find(uf[i])
            return uf[i]

        edges = []
        while len(edges) < n - 1:
            d, p1, p2 = heappop(h)
            r1, r2 = find(p1), find(p2)
            if r1 != r2:
                uf[r1] = r2
                edges.append(d)
        return sum(edges)
