"""
    File: 724.py
    Title: Find Pivot Index
    Difficulty: Easy
    URL: https://leetcode.com/problems/find-pivot-index/
"""

import unittest


from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return -1

        sum_from_left = [0] * length
        sum_from_left[0] = nums[0]
        sum_from_right = [0] * length
        sum_from_right[length - 1] = nums[length - 1]

        for i in range(1, length):
            sum_from_left[i] = sum_from_left[i - 1] + nums[i]

            back = length - 1 - i
            sum_from_right[back] = sum_from_right[back + 1] + nums[back]

        for i in range(length):
            if sum_from_left[i] == sum_from_right[i]:
                return i
        return -1


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 7, 3, 6, 5, 6]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.pivotIndex(nums), output)

    def test_example2(self):
        # Input
        nums = [1, 2, 3]
        # Output
        output = -1

        solution = Solution()
        self.assertEqual(solution.pivotIndex(nums), output)


if __name__ == "__main__":
    unittest.main()
