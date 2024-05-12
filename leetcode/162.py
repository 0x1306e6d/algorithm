"""
    File: 162.py
    Title: Find Peak Element
    Difficulty: Medium
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def peak(s, e):
            if s == e:
                return (nums[s], e)
            if e - s == 1:
                if nums[e] > nums[s]:
                    return (nums[e], e)
                else:
                    return (nums[s], s)
            mid = (s + e) // 2
            left = peak(s, mid)
            right = peak(mid + 1, e)
            if left[0] > right[0]:
                return left
            else:
                return right

        return peak(0, len(nums) - 1)[1]
