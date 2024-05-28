"""
    File: 1135.py
    Title: Connecting Cities With Minimum Cost
    Difficulty: Medium
"""

from typing import List


def heappush(h, x):
    h.append(x)
    pos = len(h) - 1
    while pos > 0:
        parent = (pos - 1) // 2
        if h[pos][0] < h[parent][0]:
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
                child = 2 * pos + 1
            else:
                break
        return first
    return last


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        h = []
        for x, y, cost in connections:
            heappush(h, (cost, x, y))

        self.uf = {}

        def find(i):
            if i not in self.uf:
                self.uf[i] = i
            if i != self.uf[i]:
                self.uf[i] = find(self.uf[i])
            return self.uf[i]

        components = n
        ans = 0
        while h:
            cost, x, y = heappop(h)
            r1, r2 = find(x), find(y)
            if r1 != r2:
                self.uf[r1] = r2
                ans += cost
                components -= 1
        if components > 1:
            return -1
        return ans
