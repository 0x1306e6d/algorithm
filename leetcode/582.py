"""
    File: 582.py
    Title: Kill Process
    Difficulty: Medium
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        root = 0
        adj = defaultdict(list)
        for v, u in zip(pid, ppid):
            if u == 0:
                root = v
            else:
                adj[u].append(v)

        ans = []
        q = deque()
        q.append(kill)
        while q:
            u = q.popleft()
            ans.append(u)

            for v in adj[u]:
                q.append(v)
        return ans
