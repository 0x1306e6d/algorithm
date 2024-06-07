"""
    File: 1615.py
    Title: Maximal Network Rank
    Difficulty: Medium
"""

from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        ans = 0
        for i in range(n):
            roads_a = adj[i]
            for j in range(i + 1, n):
                roads_b = adj[j]
                if j in roads_a:
                    ans = max(ans, len(roads_a) + len(roads_b) - 1)
                else:
                    ans = max(ans, len(roads_a) + len(roads_b))
        return ans
