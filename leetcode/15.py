"""
    File: 15.py
    Title: 3Sum
    Difficulty: Medium
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
            target = -nums[i]

            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[j] + nums[k]
                if s == target:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    j += 1
        return list(map(lambda p: [p[0], p[1], p[2]], ans))
