"""
    File: 1306.py
    Title: Jump Game III
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        q = deque()
        q.append(start)

        visited = [False] * len(arr)
        visited[start] = True

        while q:
            u = q.popleft()

            v = u + arr[u]
            if v < len(arr) and not visited[v]:
                visited[v] = True
                if arr[v] == 0:
                    return True
                q.append(v)

            v = u - arr[u]
            if v >= 0 and not visited[v]:
                visited[v] = True
                if arr[v] == 0:
                    return True
                q.append(v)
        return False
