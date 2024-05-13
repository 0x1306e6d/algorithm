"""
    File: 1168.py
    Title: Optimize Water Distribution in a Village
    Difficulty: Hard
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: List[int], pipes: List[List[int]]
    ) -> int:
        self.uf = {}

        def find(i):
            if i not in self.uf:
                self.uf[i] = i
            if i != self.uf[i]:
                self.uf[i] = find(self.uf[i])
            return self.uf[i]

        h = []
        for h1, h2, c in pipes:
            heappush(h, (c, h1, h2))

        for i in range(1, n + 1):
            heappush(h, (wells[i - 1], i, n + 1))

        ans = 0
        while h:
            c, h1, h2 = heappop(h)
            r1, r2 = find(h1), find(h2)
            if r1 == r2:
                continue

            self.uf[r1] = r2
            ans += c
        return ans
