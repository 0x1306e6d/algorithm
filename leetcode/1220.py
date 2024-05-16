"""
    File: 1220.py
    Title: Count Vowels Permutation
    Difficulty: Hard
    URL: https://leetcode.com/problems/count-vowels-permutation/
"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * 5 for _ in range(1 + n)]
        for i in range(5):
            dp[1][i] = 1
        for i in range(1, n + 1):
            dp[i][0] += (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % mod
            dp[i][1] += (dp[i - 1][0] + dp[i - 1][2]) % mod
            dp[i][2] += (dp[i - 1][1] + dp[i - 1][3]) % mod
            dp[i][3] += (dp[i - 1][2]) % mod
            dp[i][4] += (dp[i - 1][2] + dp[i - 1][3]) % mod
        return sum(dp[n]) % mod
