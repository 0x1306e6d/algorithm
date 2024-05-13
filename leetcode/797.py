"""
    File: 797.py
    Title: All Paths From Source to Target
    Difficulty: Medium
"""

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        t = len(graph) - 1

        def dfs(u, p):
            p = p + [u]
            if u == t:
                yield p
            for v in graph[u]:
                yield from dfs(v, p)

        ans = []
        for p in dfs(0, []):
            ans.append(p)
        return ans
