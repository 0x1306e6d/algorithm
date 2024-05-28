"""
    File: 354.py
    Title: Russian Doll Envelopes
    Difficulty: Hard
"""

from typing import List


def partition(arr, left, right):
    pivot = arr[right]
    idx = left
    for i in range(left, right):
        if arr[i][0] < pivot[0]:
            arr[i], arr[idx] = arr[idx], arr[i]
            idx += 1
        elif arr[i][0] == pivot[0]:
            if arr[i][1] > pivot[1]:
                arr[i], arr[idx] = arr[idx], arr[i]
                idx += 1
    arr[idx], arr[right] = arr[right], arr[idx]
    return idx


def qsort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        qsort(arr, left, pivot - 1)
        qsort(arr, pivot + 1, right)


def bisect_left(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(heights):
            dp = []
            for h in heights:
                i = bisect_left(dp, h)
                if i == len(dp):
                    dp.append(h)
                else:
                    dp[i] = h
            return len(dp)

        return lis([h for w, h in envelopes])
