"""
    File: 1658.py
    Title: Minimum Operations to Reduce X to Zero
    Difficulty: Medium
    URL: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
"""

import unittest


from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        length = len(nums)
        target = sum(nums) - x
        if target == 0:
            return length
        if target < 0:
            return -1

        i = 0
        j = 0
        subarray = 0
        max_subarray = -1
        while j < length:
            while i < j and target < subarray + nums[j]:
                subarray -= nums[i]
                i += 1
            subarray += nums[j]
            j += 1

            if subarray == target:
                max_subarray = max(max_subarray, j - i)

        if max_subarray == -1:
            return -1
        return length - max_subarray


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 1, 4, 2, 3]
        x = 5
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.minOperations(nums, x), output)

    def test_example2(self):
        # Input
        nums = [5, 6, 7, 8, 9]
        x = 4
        # Output
        output = -1

        solution = Solution()
        self.assertEqual(solution.minOperations(nums, x), output)

    def test_example3(self):
        # Input
        nums = [3, 2, 20, 1, 1, 3]
        x = 10
        # Output
        output = 5

        solution = Solution()
        self.assertEqual(solution.minOperations(nums, x), output)


if __name__ == "__main__":
    unittest.main()
