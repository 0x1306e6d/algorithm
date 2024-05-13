"""
    File: 1335.py
    Title: Minimum Difficulty of a Job Schedule
    Difficulty: Hard
"""

from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1

        self.memo = [[None] * (d + 1) for _ in range(len(jobDifficulty))]

        def dp(i, day):
            if self.memo[i][day] is not None:
                return self.memo[i][day]
            if day == d:
                self.memo[i][day] = max(jobDifficulty[i:])
                return self.memo[i][day]
            difficulty = 0
            ans = 9876543210
            for j in range(i, len(jobDifficulty) - d + day):
                difficulty = max(difficulty, jobDifficulty[j])
                ans = min(ans, difficulty + dp(j + 1, day + 1))
            self.memo[i][day] = ans
            return ans

        return dp(0, 1)
