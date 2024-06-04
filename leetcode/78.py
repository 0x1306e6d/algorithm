"""
    File: 78.py
    Title: Subsets
    Difficulty: Medium
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def backtrace(i, arr):
            if i == len(nums):
                self.ans.append(arr.copy())
            else:
                backtrace(i + 1, arr)
                arr.append(nums[i])
                backtrace(i + 1, arr)
                arr.pop()

        backtrace(0, [])

        return self.ans
