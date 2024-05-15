"""
    File: 212.py
    Title: Word Search II
    Difficulty: Hard
"""

from collections import defaultdict
from typing import List

__d__ = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        def build(w, i, node):
            if i == len(w):
                node[0] = w
                return

            c = w[i]
            if c not in node:
                node[c] = {}
            build(w, i + 1, node[c])

        trie = {}
        for w in words:
            build(w, 0, trie)

        ans = set()

        def dfs(x, y, visited, node):
            if 0 in node:
                ans.add(node[0])

            for dx, dy in __d__:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < n and 0 <= y1 < m:
                    c = board[y1][x1]
                    if c not in node:
                        continue
                    if visited[y1][x1]:
                        continue
                    visited[y1][x1] = True
                    dfs(x1, y1, visited, node[c])
                    visited[y1][x1] = False

        visited = [[False] * n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                c = board[y][x]
                if c not in trie:
                    continue
                visited[y][x] = True
                dfs(x, y, visited, trie[c])
                visited[y][x] = False
        return list(ans)
