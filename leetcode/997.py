"""
    File: 997.py
    Title: Find the Town Judge
    Difficulty: Easy
"""

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        for i in range(1, n + 1):
            if indegree[i] == (n - 1) and outdegree[i] == 0:
                return i
        return -1
