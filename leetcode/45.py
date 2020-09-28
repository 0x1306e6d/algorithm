"""
    File: 45.py
    Title: Jump Game II
    Difficulty: Hard
    URL: https://leetcode.com/problems/jump-game-ii/
"""

import unittest

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        here = 0
        there = 0
        for i in range(len(nums) - 1):
            there = max(there, i + nums[i])
            if here == i:
                count += 1
                here = there
        return count


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [2, 3, 1, 1, 4]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.jump(nums), output)


if __name__ == "__main__":
    unittest.main()
