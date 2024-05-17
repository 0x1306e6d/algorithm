"""
    File: 315.py
    Title: Count of Smaller Numbers After Self
    Difficulty: Hard
"""

from bisect import bisect_left
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        right = []
        ans = [0] * len(nums)
        for i, n in enumerate(reversed(nums)):
            j = bisect_left(right, n)
            right.insert(j, n)
            ans[len(nums) - i - 1] = j
        return ans
