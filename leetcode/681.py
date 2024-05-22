"""
    File: 681.py
    Title: Next Closest Time
    Difficulty: Medium
"""


class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour1, hour2 = int(time[0]), int(time[1])
        minute1, minute2 = int(time[3]), int(time[4])

        digits = set([hour1, hour2, minute1, minute2])

        for i in range(1, 60 * 24 + 1):
            minute2 += 1
            if minute2 >= 10:
                minute1 += 1
                minute2 = 0
            if minute1 >= 6:
                minute1 = 0
                hour2 += 1
            if hour2 >= 10:
                hour2 = 0
                hour1 += 1
            if (hour1 * 10) + hour2 >= 24:
                hour1, hour2 = 0, 0
            if (
                hour1 in digits
                and hour2 in digits
                and minute1 in digits
                and minute2 in digits
            ):
                return f"{hour1}{hour2}:{minute1}{minute2}"
