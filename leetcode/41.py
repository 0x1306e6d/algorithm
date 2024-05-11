"""
    File: 41.py
    Title: First Missing Positive
    Difficulty: Hard
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            n = nums[i]
            if n <= 0 or n > N:
                nums[i] = N + 1
        for i in range(N):
            n = abs(nums[i])
            if n > N:
                continue
            if nums[n - 1] > 0:
                nums[n - 1] *= -1
        for i in range(N):
            if nums[i] > 0:
                return i + 1
        return N + 1
