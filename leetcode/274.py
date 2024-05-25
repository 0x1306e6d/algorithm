"""
    File: 274.py
    Title: H-Index
    Difficulty: Medium
"""

from typing import List


def partition(arr, left, right):
    pivot = arr[right]
    idx = left
    for i in range(left, right):
        if arr[i] > pivot:
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
    def hIndex(self, citations: List[int]) -> int:
        qsort(citations, 0, len(citations) - 1)
        h = 0
        for i, c in enumerate(citations):
            h = max(h, min(i + 1, c))
        return h
