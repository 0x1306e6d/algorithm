"""
    File: 91.py
    Title: Decode Ways
    Difficulty: Medium
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 0 if s == "0" else 1

        s = list(map(int, s))
        memo = [0] * len(s)
        if 1 <= s[0] <= 9:
            memo[0] = 1
        for i in range(1, len(s)):
            if 1 <= s[i] <= 9:
                memo[i] += memo[i - 1]
            if 10 <= s[i - 1] * 10 + s[i] <= 26:
                if i == 1:
                    memo[i] += 1
                else:
                    memo[i] += memo[i - 2]
        return memo[-1]
