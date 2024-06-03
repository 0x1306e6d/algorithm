"""
    File: 791.py
    Title: Custom Sort String
    Difficulty: Medium
"""

from collections import defaultdict


def partition(arr, left, right, dictionary):
    pivot = arr[right]
    idx = left
    for i in range(left, right):
        if dictionary[arr[i]] < dictionary[pivot]:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1
    arr[idx], arr[right] = arr[right], arr[idx]
    return idx


def qsort(arr, left, right, dictionary):
    if left < right:
        pivot = partition(arr, left, right, dictionary)
        qsort(arr, left, pivot - 1, dictionary)
        qsort(arr, pivot + 1, right, dictionary)


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dictionary = defaultdict(int)
        for i, c in enumerate(order):
            dictionary[c] = i
        slist = list(s)
        qsort(slist, 0, len(slist) - 1, dictionary)
        return "".join(slist)
