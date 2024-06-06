"""
    File: 2466.py
    Title: Count Ways To Build Good Strings
    Difficulty: Medium
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(min(zero, one), high + 1):
            if i - zero >= 0:
                dp[i] = (dp[i] + dp[i - zero]) % mod
            if i - one >= 0:
                dp[i] = (dp[i] + dp[i - one]) % mod
        ans = 0
        for i in range(low, high + 1):
            ans = (ans + dp[i]) % mod
        return ans
