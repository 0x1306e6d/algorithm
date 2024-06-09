"""
    File: 487.py
    Title: Max Consecutive Ones II
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        q = deque()
        for i, n in enumerate(nums):
            if n == 0:
                q.append(i)
        if len(q) == 0 or len(q) == 1:
            return len(nums)
        prevprev, prev = q.popleft(), q.popleft()
        ans = prev
        while q:
            i = q.popleft()
            ans = max(ans, i - prevprev - 1)
            prevprev, prev = prev, i
        ans = max(ans, len(nums) - prevprev - 1)
        return ans
