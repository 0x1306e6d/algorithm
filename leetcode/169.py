"""
    File: 169.py
    Title: Majority Element
    Difficulty: Easy
    URL: https://leetcode.com/problems/majority-element/
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, majority = 1, nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if majority == n:
                count += 1
            else:
                if count == 0:
                    count = 1
                    majority = n
                else:
                    count -= 1
        return majority
