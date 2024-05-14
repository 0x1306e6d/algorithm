"""
    File: 1136.py
    Title: Parallel Courses
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        degree = [0] * (n + 1)
        for u, v in relations:
            adj[u].append(v)
            degree[v] += 1

        ans = 0
        q = deque()
        for i in range(1, n + 1):
            if degree[i] == 0:
                q.append(i)
        while q:
            qq = deque()
            ans += 1
            while q:
                u = q.popleft()
                for v in adj[u]:
                    degree[v] -= 1
                    if degree[v] == 0:
                        qq.append(v)
            q = qq
        if ans == 0:
            return -1
        if max(degree) > 0:
            return -1
        return ans
