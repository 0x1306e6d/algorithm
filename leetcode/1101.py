"""
    File: 1101.py
    Title: The Earliest Moment When Everyone Become Friends
    Difficulty: Medium
"""

from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        self.uf = [0] * n
        for i in range(n):
            self.uf[i] = i

        def find(i):
            if i == self.uf[i]:
                return i
            self.uf[i] = find(self.uf[i])
            return self.uf[i]

        components = n
        for t, i, j in sorted(logs, key=lambda l: l[0]):
            u, v = find(i), find(j)
            if u != v:
                self.uf[u] = v
                components -= 1
                if components == 1:
                    return t
        return -1
