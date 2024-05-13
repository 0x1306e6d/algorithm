"""
    File: 323.py
    Title: Number of Connected Components in an Undirected Graph
    Difficulty: Medium
"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.uf = [0] * n
        for i in range(n):
            self.uf[i] = i

        def find(i):
            if i == self.uf[i]:
                return i
            self.uf[i] = find(self.uf[i])
            return self.uf[i]

        ans = n
        for i, j in edges:
            u, v = find(i), find(j)
            if u != v:
                self.uf[u] = v
                ans -= 1
        return ans
