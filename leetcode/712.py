"""
    File: 712.py
    Title: Minimum ASCII Delete Sum for Two Strings
    Difficulty: Medium
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len1, len2 = len(s1), len(s2)
        memo = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            memo[i][0] = memo[i - 1][0] + ord(s1[i - 1])
        for i in range(1, len2 + 1):
            memo[0][i] = memo[0][i - 1] + ord(s2[i - 1])
        for idx1 in range(1, len1 + 1):
            for idx2 in range(1, len2 + 1):
                if s1[idx1 - 1] == s2[idx2 - 1]:
                    memo[idx1][idx2] = memo[idx1 - 1][idx2 - 1]
                else:
                    a = ord(s1[idx1 - 1]) + memo[idx1 - 1][idx2]
                    b = ord(s2[idx2 - 1]) + memo[idx1][idx2 - 1]
                    memo[idx1][idx2] = min(a, b)
        return memo[len1][len2]
