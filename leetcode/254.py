"""
    File: 254.py
    Title: Factor Combinations
    Difficulty: Medium
"""

from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def solve(num, prev):
            ans = []
            for i in range(prev, num):
                if num % i != 0:
                    continue
                q = num // i
                if q < i:
                    break
                ans.append([i, q])
                for child in solve(q, i):
                    ans.append([i] + child)
            return ans

        return solve(n, 2)
