"""
    File: 673.py
    Title: Number of Longest Increasing Subsequence
    Difficulty: Medium
"""

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = max(length)
        ans = 0
        for i in range(n):
            if length[i] == max_length:
                ans += count[i]
        return ans
