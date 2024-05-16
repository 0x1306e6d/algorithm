"""
    File: 62.py
    Title: Unique Paths
    Difficulty: Medium
    URL: https://leetcode.com/problems/unique-paths/
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if n > m:
            return self.uniquePaths(n, m)

        memo = [0] * (m + n + 1)
        memo[1] = 1
        memo[2] = 2
        for i in range(3, m + n + 1):
            memo[i] = memo[i - 1] * i
        l = m + n - 2
        r = m - 1
        return memo[l] // (memo[l - r] * memo[r])
