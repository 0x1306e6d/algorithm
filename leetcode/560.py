"""
    File: 560.py
    Title: Subarray Sum Equals K
    Difficulty: Medium
    URL: https://leetcode.com/problems/subarray-sum-equals-k/
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        current_sum = 0
        prefix_sum = defaultdict(int)
        for n in nums:
            current_sum += n

            if current_sum == k:
                ans += 1
            ans += prefix_sum[current_sum - k]

            prefix_sum[current_sum] += 1
        return ans
