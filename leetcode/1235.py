"""
    File: 1235.py
    Title: Maximum Profit in Job Scheduling
    Difficulty: Hard
"""

from functools import lru_cache
from typing import List


def bisect_left(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid][0] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def jobScheduling(
        self,
        startTime: List[int],
        endTime: List[int],
        profit: List[int],
    ) -> int:
        jobs = list(sorted(zip(startTime, endTime, profit)))

        @lru_cache
        def dp(i):
            if i == len(jobs) - 1:
                return jobs[i][2]
            if i == len(jobs):
                return 0
            end_index = bisect_left(jobs, jobs[i][1])
            return max(dp(i + 1), jobs[i][2] + dp(end_index))

        return dp(0)
