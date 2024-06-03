"""
    File: 841.py
    Title: Keys and Rooms
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        q = deque()
        q.append(0)
        visited = [False] * n
        visited[0] = True
        while q:
            u = q.popleft()
            for v in rooms[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return all(visited)
