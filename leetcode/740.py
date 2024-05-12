"""
    File: 740.py
    Title: Delete and Earn
    Difficulty: Medium
"""

from collections import defaultdict
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        for n in nums:
            points[n] += 1
        keys = list(sorted(points.keys()))

        self.memo = {}

        def dp(i):
            if i >= len(points):
                return 0
            if i in self.memo:
                return self.memo[i]

            n = keys[i]
            if i == len(points) - 1:
                self.memo[i] = n * points[n]
                return self.memo[i]

            if keys[i + 1] - n == 1:
                ans = n * points[n] + dp(i + 2)
                ans = max(ans, dp(i + 1))
            else:
                ans = n * points[n] + dp(i + 1)
            self.memo[i] = ans
            return ans

        return dp(0)
