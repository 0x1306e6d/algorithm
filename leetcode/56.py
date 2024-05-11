"""
    File: 56.py
    Title: Merge Intervals
    Difficulty: Medium
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = list(sorted(intervals))
        ans = []
        start, end = intervals[0]
        for s, e in intervals:
            if s > end:
                ans.append([start, end])
                start, end = s, e
            else:
                end = max(end, e)
        ans.append([start, end])
        return ans
