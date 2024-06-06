"""
    File: 1964.py
    Title: Find the Longest Valid Obstacle Course at Each Position
    Difficulty: Hard
"""

from typing import List


def bisect_right(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = []
        lis = []
        for i in range(n):
            height = obstacles[i]
            j = bisect_right(lis, height)
            if j == len(lis):
                lis.append(height)
            else:
                lis[j] = height
            ans.append(j + 1)
        return ans
