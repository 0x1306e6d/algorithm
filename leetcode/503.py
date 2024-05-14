"""
    File: 503.py
    Title: Next Greater Element II
    Difficulty: Medium
    URL: https://leetcode.com/problems/next-greater-element-ii/
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        for i, n in enumerate(nums):
            while stack and stack[-1][0] < n:
                _, j = stack.pop()
                ans[j] = n
            stack.append((n, i))
        for i, n in enumerate(nums):
            while stack and stack[-1][0] < n:
                _, j = stack.pop()
                ans[j] = n
        return ans
