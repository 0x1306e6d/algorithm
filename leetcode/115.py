"""
    File: 115.py
    Title: Distinct Subsequences
    Difficulty: Hard
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        lens, lent = len(s), len(t)
        memo = [[0] * (lent + 1) for _ in range(lens + 1)]

        for i in range(lens + 1):
            memo[i][0] = 1

        for i in range(1, lens + 1):
            for j in range(1, lent + 1):
                s_idx, t_idx = i - 1, j - 1
                if s[s_idx] == t[t_idx]:
                    memo[i][j] += memo[i - 1][j - 1]
                memo[i][j] += memo[i - 1][j]

        return memo[lens][lent]
