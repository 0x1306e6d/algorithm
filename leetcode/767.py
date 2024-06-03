"""
    File: 767.py
    Title: Reorganize String
    Difficulty: Medium
"""

from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def reorganizeString(self, s: str) -> str:
        chars = defaultdict(int)
        for c in s:
            chars[c] += 1

        h = []
        for c in chars:
            heappush(h, (-chars[c], c))

        ans = ""
        while h:
            first_count, first_c = heappop(h)
            first_count = -first_count - 1
            ans += first_c
            if not h:
                if first_count > 0:
                    return ""
                break

            second_count, second_c = heappop(h)
            second_count = -second_count - 1
            ans += second_c

            if first_count > 0:
                heappush(h, (-first_count, first_c))
            if second_count > 0:
                heappush(h, (-second_count, second_c))
        return ans
