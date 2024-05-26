"""
    File: 149.py
    Title: Max Points on a Line
    Difficulty: Hard
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        inf = float("inf")

        # y = ax + b
        linears = defaultdict(set)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 == x2:
                    a = inf
                else:
                    a = (y1 - y2) / (x1 - x2)
                if a == inf:
                    b = x2
                else:
                    b = y2 - a * x2

                linears[(a, b)].add((x1, y1))
                linears[(a, b)].add((x2, y2))
        ans = 0
        for key in linears:
            ans = max(ans, len(linears[key]))
        return ans
