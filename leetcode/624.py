"""
    File: 624.py
    Title: Maximum Distance in Arrays
    Difficulty: Medium
"""

from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        inf = float("inf")

        left_min, left_max = [0] * m, [0] * m
        left_min[0], left_max[0] = arrays[0][0], arrays[0][-1]
        for i in range(1, m):
            arr = arrays[i]
            left_min[i] = min(left_min[i - 1], arr[0])
            left_max[i] = max(left_max[i - 1], arr[-1])

        ans = 0
        right_min, right_max = inf, -inf
        for i in range(m - 1, 0, -1):
            arr = arrays[i]
            right_min = min(right_min, arr[0])
            right_max = max(right_max, arr[-1])
            ans = max(
                ans,
                abs(right_max - left_min[i - 1]),
                abs(left_max[i - 1] - right_min),
            )
        return ans
