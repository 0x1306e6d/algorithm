"""
    File: 698.py
    Title: Partition to K Equal Sum Subsets
    Difficulty: Medium
"""

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n, s = len(nums), sum(nums)
        if (s % k) != 0:
            return False
        target = s // k
        if max(nums) > target:
            return False

        nums.sort(reverse=True)

        visited = ["0"] * n
        memo = {}

        def backtrace(idx, count, current):
            if count == k - 1:
                return True

            if current > target:
                return False

            key = "".join(visited)
            if key in memo:
                return memo[key]

            if current == target:
                memo[key] = backtrace(0, count + 1, 0)
                return memo[key]

            for i in range(idx, n):
                if visited[i] == "0":
                    visited[i] = "1"
                    if backtrace(i + 1, count, current + nums[i]):
                        memo[key] = True
                        return True
                    visited[i] = "0"

            memo[key] = False
            return False

        return backtrace(0, 0, 0)
