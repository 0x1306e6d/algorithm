"""
    File: 228.py
    Title: Summary Ranges
    Difficulty: Easy
"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        ans = []
        a = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                pass
            else:
                if a == i - 1:
                    ans.append(str(nums[a]))
                else:
                    ans.append(f"{nums[a]}->{nums[i - 1]}")
                a = i
        if a == len(nums) - 1:
            ans.append(str(nums[a]))
        else:
            ans.append(f"{nums[a]}->{nums[len(nums) - 1]}")
        return ans
