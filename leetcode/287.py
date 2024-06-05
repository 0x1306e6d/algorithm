"""
    File: 287.py
    Title: Find the Duplicate Number
    Difficulty: Medium
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        x = nums[0]
        while x != fast:
            x = nums[x]
            fast = nums[fast]
        return x
