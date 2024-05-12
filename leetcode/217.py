"""
    File: 217.py
    Title: Contains Duplicate
    Difficulty: Easy
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
