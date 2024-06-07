"""
    File: 1589.py
    Title: Maximum Sum Obtained of Any Permutation
    Difficulty: Medium
"""

import heapq
from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        increases = [0] * n
        decreases = [0] * n
        for s, e in requests:
            increases[s] += 1
            decreases[e] += 1

        count = 0
        counts = [0] * n
        for i, (inc, dec) in enumerate(zip(increases, decreases)):
            count += inc
            counts[i] = count
            count -= dec

        h = []
        for i, count in enumerate(counts):
            if count > 0:
                heapq.heappush(h, -count)

        nums.sort(reverse=True)

        ans = 0
        i = 0
        while h:
            count = heapq.heappop(h)
            count = -count
            ans = (ans + (nums[i] * count)) % mod
            i += 1
        return ans
