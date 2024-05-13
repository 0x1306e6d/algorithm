"""
    File: 547.py
    Title: Number of Provinces
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        ans = 0
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            ans += 1
            visited[i] = True

            q = deque()
            q.append(i)
            while q:
                u = q.pop()
                for v in range(n):
                    if not visited[v] and isConnected[u][v] == 1:
                        visited[v] = True
                        q.append(v)
        return ans
