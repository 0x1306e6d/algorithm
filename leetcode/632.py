"""
    File: 632.py
    Title: Smallest Range Covering Elements from K Lists
    Difficulty: Hard
"""

from typing import List


def heappush(h, x):
    h.append(x)
    pos = len(h) - 1
    while pos > 0:
        parent = (pos - 1) // 2
        if h[parent][0] > h[pos][0]:
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
            if right < len(h) and h[child][0] > h[right][0]:
                child = right
            if h[pos][0] > h[child][0]:
                h[pos], h[child] = h[child], h[pos]
                pos = child
                child = pos * 2 + 1
            else:
                break
        return first
    return last


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        inf = float("inf")

        board = [None] * k
        fill = set()

        heap = []
        for i, nnums in enumerate(nums):
            for n in nnums:
                heappush(heap, (n, i))

        all_fill = False
        a, b = -inf, inf
        minimum = None
        while heap:
            n, i = heappop(heap)

            m = board[i]
            board[i] = n

            fill.add(i)
            all_fill = all_fill or len(fill) == k

            if all_fill:
                if minimum is None or minimum == m:
                    minimum = min(board)
                c, d = minimum, n
                if d - c < b - a:
                    a, b = c, d
        return [a, b]
