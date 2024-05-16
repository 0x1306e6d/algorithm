"""
    File: 918.py
    Title: Maximum Sum Circular Subarray
    Difficulty: Medium
"""

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        r = nums[-1]
        right = [0] * len(nums)
        right[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            r += nums[i]
            right[i] = max(right[i + 1], r)

        current, best = 0, -float("inf")
        l = 0
        special = -float("inf")
        for i, n in enumerate(nums):
            current = max(current + n, n)
            best = max(best, current)

            l += n
            if i < len(nums) - 1:
                special = max(special, l + right[i + 1])
        return max(best, special)
