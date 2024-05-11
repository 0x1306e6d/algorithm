"""
    File: 210.py
    Title: Course Schedule II
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            degree[a] += 1
            adj[b].append(a)

        ans = []
        q = deque()
        visited = [False] * numCourses
        for i, d in enumerate(degree):
            if d == 0:
                visited[i] = True
                q.append(i)
        while q:
            u = q.pop()
            ans.append(u)
            for v in adj[u]:
                degree[v] -= 1
                if degree[v] == 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)
        if len(ans) != numCourses:
            return []
        return ans
