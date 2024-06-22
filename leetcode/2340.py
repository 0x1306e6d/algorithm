"""
    File: 2340.py
    Title: Minimum Adjacent Swaps to Make a Valid Array
    Difficulty: Medium
"""

from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        largest, smallest = 0, 0
        for i, num in enumerate(nums):
            if num >= nums[largest]:
                largest = i
            if num < nums[smallest]:
                smallest = i
        ans = smallest + len(nums) - largest - 1
        if smallest > largest:
            return ans - 1
        return ans
