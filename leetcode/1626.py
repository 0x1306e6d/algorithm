"""
    File: 1626.py
    Title: Best Team With No Conflicts
    Difficulty: Medium
"""

from functools import cache
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [[0, 0] for _ in range(len(scores))]
        for i in range(len(scores)):
            players[i][0] = ages[i]
            players[i][1] = scores[i]
        players.sort()

        @cache
        def dp(prev, current):
            if current >= len(players):
                return 0

            ans = dp(prev, current + 1)

            if prev is not None and players[current][1] < players[prev][1]:
                return ans

            return max(ans, players[current][1] + dp(current, current + 1))

        return dp(None, 0)
