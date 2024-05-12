"""
    File: 347.py
    Title: Top K Frequent Elements
    Difficulty: Medium
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = list(sorted(nums))

        h = []
        num = nums[0]
        freq = 1
        for i in range(1, len(nums)):
            n = nums[i]
            if num == n:
                freq += 1
            else:
                heappush(h, (-freq, num))
                num = n
                freq = 1
        heappush(h, (-freq, num))

        ans = []
        for i in range(k):
            p = heappop(h)
            ans.append(p[1])
        return ans
