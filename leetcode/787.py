"""
    File: 787.py
    Title: Cheapest Flights Within K Stops
    Difficulty: Medium
"""

from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = [[] for _ in range(n)]
        for u, v, p in flights:
            adj[u].append((v, p))

        inf = 9876543210
        distance = [inf] * n
        distance[src] = 0

        prev = [(src, 0)]
        for _ in range(k + 2):
            curr = []

            for u, d1 in prev:
                if distance[u] < d1:
                    continue
                distance[u] = d1

                for v, d2 in adj[u]:
                    curr.append((v, d1 + d2))

            prev = curr

        if distance[dst] == inf:
            return -1
        return distance[dst]
