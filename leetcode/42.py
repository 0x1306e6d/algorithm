"""
    File: 42.py
    Title: Trapping Rain Water
    Difficulty: Hard
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_memo = [0] * len(height)
        left_memo[0] = height[0]
        right_memo = [0] * len(height)
        right_memo[-1] = height[-1]
        for i in range(1, len(height)):
            left_memo[i] = max(left_memo[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            right_memo[i] = max(right_memo[i + 1], height[i])
        ans = 0
        for i in range(len(height)):
            ans += min(left_memo[i], right_memo[i]) - height[i]
        return ans
