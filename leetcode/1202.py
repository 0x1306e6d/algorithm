"""
    File: 1202.py
    Title: Smallest String With Swaps
    Difficulty: Medium
"""

from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.uf = [0] * n
        for i in range(n):
            self.uf[i] = i

        def find(i):
            if i == self.uf[i]:
                return i
            self.uf[i] = find(self.uf[i])
            return self.uf[i]

        for a, b in pairs:
            u, v = find(a), find(b)
            if u != v:
                self.uf[u] = v

        components = defaultdict(str)
        for i in range(n):
            r = find(i)
            components[r] += s[i]
        for i in components:
            components[i] = sorted(components[i])

        ans = ""
        for i in range(n):
            r = find(i)
            ans += components[r][0]
            components[r].pop(0)
        return ans
