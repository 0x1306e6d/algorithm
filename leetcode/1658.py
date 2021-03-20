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
        s = sum(nums)

        target = s - x

        max_subarray = 0
        for i in range(len(nums)):
            count = 1
            next_s = nums[i]
            for j in range(i + 1, len(nums)):
                if next_s == target:
                    break
                next_s += nums[j]
                count += 1
            if next_s == target:
                max_subarray = max(max_subarray, count)
        if max_subarray == 0:
            return -1
        return len(nums) - max_subarray


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
