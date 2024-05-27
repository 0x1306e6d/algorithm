"""
    File: 763.py
    Title: Partition Labels
    Difficulty: Medium
"""

from typing import List


def partition(arr, left, right):
    pivot_start, pivot_end = arr[right]
    idx = left
    for i in range(left, right):
        start, end = arr[i]
        if start < pivot_start:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1
        elif start == pivot_start:
            if end < pivot_end:
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
    def partitionLabels(self, s: str) -> List[int]:
        start = {}
        end = {}
        for i, c in enumerate(s):
            if c not in start:
                start[c] = end[c] = i
            else:
                end[c] = i

        intervals = []
        for c in start:
            intervals.append((start[c], end[c]))
        qsort(intervals, 0, len(intervals) - 1)

        ans = []
        min_start, max_end = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start > max_end:
                ans.append(max_end - min_start + 1)
                min_start, max_end = start, end
            else:
                max_end = max(max_end, end)
        ans.append(max_end - min_start + 1)
        return ans
