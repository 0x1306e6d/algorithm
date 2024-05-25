"""
    File: 57.py
    Title: Insert Interval
    Difficulty: Medium
"""

from typing import List


class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int],
    ) -> List[List[int]]:
        new_start, new_end = newInterval

        ans = []
        min_start, max_end = new_start, new_end
        put = False
        for start, end in intervals:
            if end < new_start:
                ans.append([start, end])
            elif start > new_end:
                if not put:
                    ans.append([min_start, max_end])
                    put = True
                ans.append([start, end])
            else:
                min_start = min(min_start, start)
                max_end = max(max_end, end)
        if not put:
            ans.append([min_start, max_end])
        return ans
