"""
    File: 493.py
    Title: Reverse Pairs
    Difficulty: Hard
    URL: https://leetcode.com/problems/reverse-pairs/
"""

import unittest

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0

        keys = []
        for num in nums:
            index = self.bsearch(keys, (num * 2) + 1)
            ans += len(keys) - index
            keys.insert(self.bsearch(keys, num), num)

        return ans

    def bsearch(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 3, 2, 3, 1]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.reversePairs(nums), output)

    def test_example2(self):
        # Input
        nums = [2, 4, 3, 5, 1]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.reversePairs(nums), output)


if __name__ == "__main__":
    unittest.main()
