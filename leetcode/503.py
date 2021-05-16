"""
    File: 503.py
    Title: Next Greater Element II
    Difficulty: Medium
    URL: https://leetcode.com/problems/next-greater-element-ii/
"""

import unittest

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack = []
        for i in range(2 * len(nums)):
            j = i % len(nums)
            while stack and nums[j] > nums[stack[-1]]:
                ans[stack[-1]] = nums[j]
                stack.pop()
            stack.append(j)
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 2, 1]
        # Output
        output = [2, -1, 2]

        solution = Solution()
        self.assertEqual(solution.nextGreaterElements(nums), output)

    def test_example2(self):
        # Input
        nums = [1, 2, 3, 4, 3]
        # Output
        output = [2, 3, 4, -1, 4]

        solution = Solution()
        self.assertEqual(solution.nextGreaterElements(nums), output)


if __name__ == "__main__":
    unittest.main()
