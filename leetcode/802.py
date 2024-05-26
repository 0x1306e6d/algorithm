"""
    File: 802.py
    Title: Find Eventual Safe States
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        degree = [0] * n
        reverse = [[] for _ in range(n)]
        for u in range(n):
            for v in graph[u]:
                degree[u] += 1
                reverse[v].append(u)

        safe = []
        q = deque()
        for u in range(n):
            if degree[u] == 0:
                q.append(u)
        while q:
            u = q.popleft()
            safe.append(u)

            for v in reverse[u]:
                degree[v] -= 1
                if degree[v] == 0:
                    q.append(v)
        return list(sorted(safe))
