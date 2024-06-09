"""
    File: 1057.py
    Title: Campus Bikes
    Difficulty: Medium
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def assignBikes(
        self,
        workers: List[List[int]],
        bikes: List[List[int]],
    ) -> List[int]:
        def manhattan(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        h = []
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, bw) in enumerate(bikes):
                distance = manhattan(wx, wy, bx, bw)
                heappush(h, (distance, i, j))

        ans = [None] * len(workers)
        visited = [False] * len(bikes)
        while h:
            _, worker, bike = heappop(h)
            if ans[worker] is not None or visited[bike]:
                continue
            ans[worker] = bike
            visited[bike] = True
        return ans
