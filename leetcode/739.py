"""
    File: 739.py
    Title: Daily Temperatures
    Difficulty: Medium
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((t, i))
                continue
            while stack and stack[-1][0] < t:
                tt, j = stack.pop()
                ans[j] = i - j
            stack.append((t, i))
        return ans
