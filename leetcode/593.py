"""
    File: 593.py
    Title: Valid Square
    Difficulty: Medium
"""

from collections import defaultdict
from typing import List


class Solution:
    def validSquare(
        self,
        p1: List[int],
        p2: List[int],
        p3: List[int],
        p4: List[int],
    ) -> bool:
        def distance(p, q):
            a = abs(p[0] - q[0])
            b = abs(p[1] - q[1])
            return a * a + b * b

        distances = defaultdict(int)
        distances[distance(p1, p2)] += 1
        distances[distance(p1, p3)] += 1
        distances[distance(p1, p4)] += 1
        distances[distance(p2, p3)] += 1
        distances[distance(p2, p4)] += 1
        distances[distance(p3, p4)] += 1
        diagonal = max(distances)
        side = min(distances)
        return distances[diagonal] == 2 and distances[side] == 4
