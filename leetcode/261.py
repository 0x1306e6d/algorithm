"""
    File: 261.py
    Title: Graph Valid Tree
    Difficulty: Medium
"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.uf = [0] * n
        for i in range(n):
            self.uf[i] = i
        self.ranks = [0] * n
        self.count = n

        def find(i):
            if i == self.uf[i]:
                return self.uf[i]
            self.uf[i] = find(self.uf[i])
            return self.uf[i]

        def union(i, j):
            u, v = find(i), find(j)
            if u != v:
                if self.ranks[u] > self.ranks[v]:
                    self.uf[v] = u
                elif self.ranks[u] < self.ranks[v]:
                    self.uf[u] = v
                else:
                    self.uf[u] = v
                    self.ranks[v] += 1
                self.count -= 1
                return True
            else:
                return False

        for u, v in edges:
            if not union(u, v):
                return False
        return self.count == 1
