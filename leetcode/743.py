"""
    File: 743.py
    Title: Network Delay Time
    Difficulty: Medium
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = 9876543210

        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            heappush(adj[u], (w, v))

        distance = [inf] * (n + 1)
        pq = [(0, k)]
        while pq:
            d1, u = heappop(pq)

            if d1 > distance[u]:
                continue
            distance[u] = d1

            while adj[u]:
                d2, v = heappop(adj[u])
                d = d1 + d2
                if d < distance[v]:
                    heappush(pq, (d, v))

        ans = 0
        for i in range(1, n + 1):
            d = distance[i]
            if d == inf:
                return -1
            ans = max(ans, d)
        return ans
