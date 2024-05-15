"""
    File: 502.py
    Title: IPO
    Difficulty: Hard
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def findMaximizedCapital(
        self,
        k: int,
        w: int,
        profits: List[int],
        capital: List[int],
    ) -> int:
        h = []
        for p, c in zip(profits, capital):
            if c >= p:
                pass
            heappush(h, (-p, c))

        count = 0
        dlq = []
        while h and count < k:
            p, c = heappop(h)
            if c > w:
                heappush(dlq, (c, p))
            else:
                w += -p
                count += 1

                while dlq and dlq[0][0] <= w:
                    cc, pp = heappop(dlq)
                    heappush(h, (pp, cc))
        return w
