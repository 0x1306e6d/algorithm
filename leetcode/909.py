"""
    File: 909.py
    Title: Snakes and Ladders
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        end = n * n
        inf = float("inf")

        label = 1
        graph = [0] * (end + 1)
        reverse = False
        for y in range(n - 1, -1, -1):
            if reverse:
                cols = reversed(board[y])
            else:
                cols = board[y]
            for col in cols:
                if col == -1:
                    graph[label] = label
                else:
                    graph[label] = col
                label += 1
            reverse = not reverse

        q = deque()
        q.append((0, 1))
        visited = [inf] * (end + 1)
        while q:
            moves, pos = q.popleft()
            if pos == end:
                return moves
            for i in range(pos + 1, min(pos + 6, end) + 1):
                if moves + 1 < visited[graph[i]]:
                    visited[graph[i]] = moves + 1
                    q.append((moves + 1, graph[i]))
        return -1
