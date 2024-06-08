"""
    File: 785.py
    Title: Is Graph Bipartite?
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for i in range(len(graph)):
            if i in colors:
                continue
            colors[i] = 0
            q = deque()
            q.append(i)
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in colors:
                        colors[v] = colors[u] ^ 1
                        q.append(v)
                    elif colors[v] == colors[u]:
                        return False
        return True
