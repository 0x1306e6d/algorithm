"""
    File: 253.py
    Title: Meeting Rooms II
    Difficulty: Medium
"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals = sorted(intervals)
        while intervals:
            new_intervals = []
            end = 0
            for s, e in intervals:
                if s >= end:
                    end = e
                else:
                    new_intervals.append([s, e])
            ans += 1
            intervals = new_intervals
        return ans
