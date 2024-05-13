"""
    File: 1971.py
    Title: Find if Path Exists in Graph
    Difficulty: Easy
"""

from typing import List


class Solution:
    def validPath(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
    ) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u, visited):
            if u == destination:
                return True
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if dfs(v, visited):
                        return True
            return False

        return dfs(source, [False] * n)
