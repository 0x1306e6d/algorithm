"""
    File: 79.py
    Title: Word Search
    Difficulty: Medium
"""

from typing import List

__dx__ = (0, 0, -1, 1)
__dy__ = (-1, 1, 0, 0)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(x, y, l, visited):
            if l == len(word):
                return True

            for dx, dy in zip(__dx__, __dy__):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m:
                    if board[y2][x2] != word[l]:
                        continue
                    if visited[y2][x2]:
                        continue
                    visited[y2][x2] = True
                    if dfs(x2, y2, l + 1, visited):
                        return True
                    visited[y2][x2] = False
            return False

        for y in range(m):
            for x in range(n):
                if board[y][x] != word[0]:
                    continue
                visited = [[False] * n for _ in range(m)]
                visited[y][x] = True
                if dfs(x, y, 1, visited):
                    return True
        return False
