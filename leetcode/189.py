"""
    File: 189.py
    Title: Rotate Array
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        q = deque()
        for i in range(len(nums) - k, len(nums)):
            q.append(nums[i])
        for i in range(len(nums)):
            q.append(nums[i])
            n = q.popleft()
            nums[i] = n
