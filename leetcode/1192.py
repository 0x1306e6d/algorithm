"""
    File: 1192.py
    Title: Critical Connections in a Network
    Difficulty: Hard
"""

from collections import defaultdict
from typing import List


inf = float("inf")


class Solution:
    def criticalConnections(
        self,
        n: int,
        connections: List[List[int]],
    ) -> List[List[int]]:
        rank = {}
        graph = defaultdict(list)
        connections_set = set()
        for i in range(n):
            rank[i] = None
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            connections_set.add((min(u, v), max(u, v)))

        def dfs(u, r, parent):
            if rank[u] is not None:
                return rank[u]

            rank[u] = r

            ans = inf
            for v in graph[u]:
                if v == parent:
                    continue
                r2 = dfs(v, r + 1, u)
                if r2 <= r:
                    connections_set.remove((min(u, v), max(u, v)))
                ans = min(ans, r2)
            return ans

        dfs(0, 0, None)

        return list(connections_set)
