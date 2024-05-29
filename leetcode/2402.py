"""
    File: 2402.py
    Title: Meeting Rooms III
    Difficulty: Hard
"""

from collections import deque
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        inf = float("inf")

        ans = [0] * n
        rooms = [0] * n

        q = deque()
        for s, e in sorted(meetings):
            q.append((s, e - s))
        while q:
            s, p = q.popleft()
            e = s + p
            wait = True
            min_end = inf
            for i, room in enumerate(rooms):
                if room <= s:
                    wait = False
                    ans[i] += 1
                    rooms[i] = e
                    break
                min_end = min(min_end, room)
            if wait:
                q.appendleft((min_end, p))

        i = 0
        hold = 0
        for j, m in enumerate(ans):
            if m > hold:
                i = j
                hold = m
        return i
