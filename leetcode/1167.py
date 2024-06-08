"""
    File: 1167.py
    Title: Minimum Cost to Connect Sticks
    Difficulty: Medium
"""

from typing import List


def heappush(h, x):
    h.append(x)
    pos = len(h) - 1
    while pos > 0:
        parent = (pos - 1) // 2
        if h[pos] < h[parent]:
            h[pos], h[parent] = h[parent], h[pos]
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
            if right < len(h) and h[right] < h[child]:
                child = right
            if h[child] < h[pos]:
                h[pos], h[child] = h[child], h[pos]
                pos = child
                child = 2 * pos + 1
            else:
                break
        return first
    return last


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        h = []
        for stick in sticks:
            heappush(h, stick)

        ans = 0
        while h:
            x = heappop(h)
            if not h:
                break
            y = heappop(h)
            ans += x + y
            heappush(h, x + y)
        return ans
