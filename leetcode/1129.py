"""
    File: 1129.py
    Title: Shortest Path with Alternating Colors
    Difficulty: Medium
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(
        self,
        n: int,
        redEdges: List[List[int]],
        blueEdges: List[List[int]],
    ) -> List[int]:
        adj = defaultdict(list)
        for u, v in redEdges:
            adj[u].append((v, 0))
        for u, v in blueEdges:
            adj[u].append((v, 1))

        ans = [-1] * n
        ans[0] = 0

        q = deque()
        q.append((0, 0, None))

        visited = [[False, False] for _ in range(n)]
        visited[0][0] = visited[0][1] = True

        while q:
            u, path, color = q.popleft()
            if ans[u] == -1:
                ans[u] = path

            for v, next_color in adj[u]:
                if color == next_color or visited[v][next_color]:
                    continue
                visited[v][next_color] = True
                q.append((v, path + 1, next_color))

        return ans
