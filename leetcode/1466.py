"""
    File: 1466.py
    Title: Reorder Routes to Make All Paths Lead to the City Zero
    Difficulty: Medium
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append((b, True))
            adj[b].append((a, False))

        q = deque()
        q.append(0)
        visited = [False] * n
        visited[0] = True

        ans = 0
        while q:
            u = q.popleft()

            for v, reverse in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if reverse:
                        ans += 1
                    q.append(v)
        return ans
