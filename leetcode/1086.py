"""
    File: 1086.py
    Title: High Five
    Difficulty: Easy
"""

from collections import defaultdict
from typing import List


def heappush(h, x):
    h.append(x)
    pos = len(h) - 1
    while pos > 0:
        parent = (pos - 1) // 2
        if h[pos] > h[parent]:
            h[parent], h[pos] = h[pos], h[parent]
            pos = parent
        else:
            break


def heappop(h):
    last = h.pop()
    if h:
        first = h[0]
        h[0] = last
        pos, child = 0, 1
        while child < len(h):
            right = child + 1
            if right < len(h) and h[child] < h[right]:
                child = right
            if h[pos] < h[child]:
                h[pos], h[child] = h[child], h[pos]
                pos, child = child, 2 * child + 1
            else:
                break
        return first
    return last


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for id, score in items:
            heappush(scores[id], score)

        ans = []
        for id in sorted(scores):
            score_sum = 0
            for _ in range(5):
                score_sum += heappop(scores[id])
            ans.append([id, score_sum // 5])
        return ans
