"""
    File: 34.py
    Title: Find First and Last Position of Element in Sorted Array
    Difficulty: Medium
"""

from typing import List


def bisect_left(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


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
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        start = bisect_left(nums, target)
        end = bisect_right(nums, target)
        if start >= len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, end - 1]
