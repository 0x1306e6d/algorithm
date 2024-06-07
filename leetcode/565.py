"""
    File: 565.py
    Title: Array Nesting
    Difficulty: Medium
    URL: https://leetcode.com/problems/array-nesting/
"""

from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            count = 0
            k = i
            while k != nums[k] and not visited[k]:
                visited[k] = True
                k = nums[k]
                count += 1
            ans = max(ans, count)
        return ans
