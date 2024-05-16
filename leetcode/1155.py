"""
    File: 1155.py
    Title: Number of Dice Rolls With Target Sum
    Difficulty: Medium
"""


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (target + 1)
        for i in range(1, k + 1):
            if i <= target:
                dp[i] = 1
        for _ in range(2, n + 1):
            new_dp = [0] * (target + 1)
            for i in range(1, target + 1):
                for j in range(1, k + 1):
                    if i - j >= 0:
                        new_dp[i] = (new_dp[i] + dp[i - j]) % mod
            dp = new_dp
        return dp[target]
