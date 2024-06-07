"""
    File: 1228.py
    Title: Missing Number In Arithmetic Progression
    Difficulty: Easy
"""

from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        a, b = arr[1] - arr[0], arr[2] - arr[1]
        if a == b:
            gap = a
        elif abs(a) > abs(b):
            gap = b
        else:
            gap = a

        if gap == 0:
            return arr[0]

        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != gap:
                return arr[i - 1] + gap
