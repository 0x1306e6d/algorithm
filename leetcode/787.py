"""
    File: 787.py
    Title: Cheapest Flights Within K Stops
    Difficulty: Medium
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = [[] for _ in range(n)]
        for f, t, p in flights:
            adj[f].append((t, p))

        heap = [(0, src, k + 1)]
        visited = [[False] * (k + 2) for _ in range(n)]
        while heap:
            d, u, kk = heappop(heap)
            if kk < 0:
                continue
            if u == dst:
                return d
            if visited[u][kk]:
                continue
            visited[u][kk] = True
            for v, w in adj[u]:
                heappush(heap, (d + w, v, kk - 1))
        return -1
