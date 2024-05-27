"""
    File: 505.py
    Title: The Maze II
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
            else:
                break
        return first
    return last


class Solution:
    def shortestDistance(
        self,
        maze: List[List[int]],
        start: List[int],
        destination: List[int],
    ) -> int:
        inf = float("inf")
        direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        m, n = len(maze), len(maze[0])

        start_y, start_x = start
        destination_y, destination_x = destination

        h = [(0, start_x, start_y)]
        visited = [[inf] * n for _ in range(m)]
        visited[start_y][start_x] = 0
        while h:
            d1, x1, y1 = heappop(h)
            if x1 == destination_x and y1 == destination_y:
                return d1

            for dx, dy in direction:
                d2 = 1
                x2, y2 = x1 + dx, y1 + dy
                if 0 <= x2 < n and 0 <= y2 < m and maze[y2][x2] != 1:
                    while True:
                        d2 += 1
                        x2, y2 = x2 + dx, y2 + dy
                        if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m or maze[y2][x2] == 1:
                            d2 -= 1
                            x2, y2 = x2 - dx, y2 - dy
                            break

                    d = d1 + d2
                    if visited[y2][x2] > d:
                        visited[y2][x2] = d
                        heappush(h, (d, x2, y2))
        return -1
