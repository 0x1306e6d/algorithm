"""
    File: 2140.py
    Title: Solving Questions With Brainpower
    Difficulty: Medium
"""

from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[n - 1] = questions[n - 1][0]
        for i in range(n - 2, -1, -1):
            point, brainpower = questions[i]
            if i + brainpower + 1 < n:
                dp[i] = max(dp[i + 1], point + dp[i + brainpower + 1])
            else:
                dp[i] = max(dp[i + 1], point)
        return dp[0]
