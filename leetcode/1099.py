"""
    File: 1099.py
    Title: Two Sum Less Than K
    Difficulty: Easy
"""

from typing import List


def partition(arr, left, right):
    pivot = arr[right]
    idx = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[idx] = arr[idx], arr[i]
            idx += 1
    arr[idx], arr[right] = arr[right], arr[idx]
    return idx


def qsort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        qsort(arr, left, pivot - 1)
        qsort(arr, pivot + 1, right)


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        qsort(nums, 0, len(nums) - 1)

        ans = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if s < k:
                    ans = max(ans, s)
                else:
                    break
        return ans
