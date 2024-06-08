"""
    File: 252.py
    Title: Meeting Rooms
    Difficulty: Easy
"""

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        time = 0
        for s, e in intervals:
            if s < time:
                return False
            time = e
        return True
