"""
    File: 436.py
    Title: Find Right Interval
    Difficulty: Medium
"""

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
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        for i, (start, end) in enumerate(intervals):
            starts.append((start, i))
        starts.sort()

        ans = []
        for start, end in intervals:
            j = bisect_left(starts, end)
            if j == len(starts):
                ans.append(-1)
            else:
                ans.append(starts[j][1])
        return ans
