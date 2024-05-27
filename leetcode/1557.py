"""
    File: 1557.py
    Title: Minimum Number of Vertices to Reach All Nodes
    Difficulty: Medium
"""

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1

        ans = []
        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)
        return ans
