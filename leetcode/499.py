"""
    File: 499.py
    Title: The Maze III
    Difficulty: Hard
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def findShortestWay(
        self,
        maze: List[List[int]],
        ball: List[int],
        hole: List[int],
    ) -> str:
        m, n = len(maze), len(maze[0])
        directions = [("d", 0, 1), ("l", -1, 0), ("r", 1, 0), ("u", 0, -1)]
        inf = float("inf")

        ball_y, ball_x = ball
        hole_y, hole_x = hole

        h = []
        heappush(h, (0, [], ball_x, ball_y))
        visited = [[inf] * n for _ in range(m)]
        ans = []
        ans_distance = inf
        while h:
            distance, path, x1, y1 = heappop(h)

            for d, dx, dy in directions:
                x2, y2 = x1 + dx, y1 + dy
                if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m or maze[y2][x2] == 1:
                    continue
                new_distance = distance + 1
                while 0 <= x2 < n and 0 <= y2 < m and maze[y2][x2] != 1:
                    if x2 == hole_x and y2 == hole_y:
                        if new_distance < ans_distance:
                            ans = ["".join(path) + d]
                            ans_distance = new_distance
                        elif new_distance == ans_distance:
                            ans.append("".join(path) + d)
                    x2 += dx
                    y2 += dy
                    new_distance += 1
                x2 -= dx
                y2 -= dy
                new_distance -= 1
                if new_distance > visited[y2][x2]:
                    continue
                visited[y2][x2] = new_distance
                new_path = path.copy()
                new_path.append(d)
                heappush(h, (new_distance, new_path, x2, y2))
        if len(ans) == 0:
            return "impossible"
        ans.sort()
        return ans[0]
