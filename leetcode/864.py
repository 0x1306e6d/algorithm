"""
    File: 864.py
    Title: Shortest Path to Get All Keys
    Difficulty: Hard
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
            if right < len(h) and h[right][0] < h[child][0]:
                child = right
            if h[child][0] < h[pos][0]:
                h[pos], h[child] = h[child], h[pos]
                pos = child
                child = 2 * pos + 1
            else:
                break
        return first
    return last


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        start_x = start_y = 0
        keys = set()
        for y in range(m):
            for x in range(n):
                c = grid[y][x]
                if "a" <= c <= "z":
                    keys.add(c)
                elif c == "@":
                    start_x, start_y = x, y

        visited = [[False] * n for _ in range(m)]
        visited[start_y][start_x] = True
        h = [(0, start_x, start_y, visited, set())]
        while h:
            ans, x1, y1, visited, acquired = heappop(h)

            c = grid[y1][x1]
            if "a" <= c <= "z" and c not in acquired:
                acquired = acquired.copy()
                acquired.add(c)
                if len(acquired) == len(keys):
                    return ans
                visited = [[False] * n for _ in range(m)]
                visited[y1][x1] = True

            for dx, dy in directions:
                x2, y2 = x1 + dx, y1 + dy
                if 0 <= x2 < n and 0 <= y2 < m:
                    if visited[y2][x2]:
                        continue
                    c = grid[y2][x2]
                    if c == "#":
                        continue
                    if "A" <= c <= "Z" and c.lower() not in acquired:
                        continue
                    visited[y2][x2] = True
                    heappush(h, (ans + 1, x2, y2, visited, acquired))
        return -1
