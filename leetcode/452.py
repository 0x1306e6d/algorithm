"""
    File: 452.py
    Title: Minimum Number of Arrows to Burst Balloons
    Difficulty: Medium
"""

from typing import List


def partition(arr, left, right):
    pivot = arr[right]
    idx = left
    for i in range(left, right):
        if arr[i][0] < pivot[0]:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1
        elif arr[i][0] == pivot[0] and arr[i][1] < pivot[1]:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1
    arr[idx], arr[right] = arr[right], arr[idx]
    return idx


def qsort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        qsort(arr, left, pivot - 1)
        qsort(arr, pivot + 1, right)


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        qsort(points, 0, len(points) - 1)
        arrows = 1
        start1, end1 = points[0]
        for i in range(1, len(points)):
            start2, end2 = points[i]
            if start1 <= start2 <= end1:
                end1 = min(end1, end2)
            else:
                arrows += 1
                start1, end1 = start2, end2
        return arrows
