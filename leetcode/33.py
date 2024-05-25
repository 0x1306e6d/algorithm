"""
    File: 33.py
    Title: Search in Rotated Sorted Array
    Difficulty: Medium
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_k(lo, hi):
            if nums[lo] < nums[hi]:
                return 0
            if lo == hi:
                return lo
            if lo + 1 == hi:
                return lo

            mid = (lo + hi) // 2
            if nums[lo] < nums[mid]:
                return find_k(mid, hi)
            return find_k(lo, mid)

        def bs(lo, hi):
            if lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return bs(lo, mid - 1)
                else:
                    return bs(mid + 1, hi)
            else:
                return None

        k = find_k(0, len(nums) - 1)
        ans = bs(0, k)
        if ans is not None:
            return ans
        ans = bs(k + 1, len(nums) - 1)
        if ans is not None:
            return ans
        return -1
