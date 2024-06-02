"""
    File: 2444.py
    Title: Count Subarrays With Fixed Bounds
    Difficulty: Hard
"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_idx = max_idx = oor_idx = -1
        for i, n in enumerate(nums):
            if n == minK:
                min_idx = i
            if n == maxK:
                max_idx = i
            if n < minK or n > maxK:
                oor_idx = i
            at_least = min(min_idx, max_idx)
            if oor_idx >= at_least:
                continue
            ans += at_least - oor_idx
        return ans
