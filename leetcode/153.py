"""
    File: 153.py
    Title: Find Minimum in Rotated Sorted Array
    Difficulty: Medium
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find(left, right):
            if nums[left] <= nums[right]:
                return left
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                return find(mid + 1, right)
            return find(left, mid)

        idx = find(0, len(nums) - 1)
        return nums[idx]
