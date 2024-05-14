"""
    File: 97.py
    Title: Interleaving String
    Difficulty: Medium
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if len(s3) == 0:
            return False

        n, m = len(s1), len(s2)
        memo = [[None] * (m + 1) for _ in range(n + 1)]

        def dp(i1, i2):
            if memo[i1][i2] is not None:
                return memo[i1][i2]
            ans = False
            i3 = i1 + i2
            if i3 >= len(s3):
                memo[i1][i2] = False
                return memo[i1][i2]
            if i1 == n:
                memo[i1][i2] = s2[i2:] == s3[i3:]
                return memo[i1][i2]
            if i2 == m:
                memo[i1][i2] = s1[i1:] == s3[i3:]
                return memo[i1][i2]
            if s1[i1] == s3[i3]:
                ans = dp(i1 + 1, i2)
                if ans:
                    return True
            if s2[i2] == s3[i3]:
                ans = dp(i1, i2 + 1)
                if ans:
                    return True
            memo[i1][i2] = False
            return False

        return dp(0, 0)
