"""
    File: 1470.py
    Title: Shuffle the Array
    Difficulty: Easy
    URL: https://leetcode.com/problems/shuffle-the-array/
"""

import unittest

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        x = 0
        y = n
        for i in range(n):
            ans.append(nums[x])
            x += 1
            ans.append(nums[y])
            y += 1
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [2, 5, 1, 3, 4, 7]
        n = 3
        # Output
        output = [2, 3, 5, 4, 1, 7]

        solution = Solution()
        self.assertEqual(solution.shuffle(nums, n), output)

    def test_example2(self):
        # Input
        nums = [1, 2, 3, 4, 4, 3, 2, 1]
        n = 4
        # Output
        output = [1, 4, 2, 3, 3, 2, 4, 1]

        solution = Solution()
        self.assertEqual(solution.shuffle(nums, n), output)

    def test_example3(self):
        # Input
        nums = [1, 1, 2, 2]
        n = 2
        # Output
        output = [1, 2, 1, 2]

        solution = Solution()
        self.assertEqual(solution.shuffle(nums, n), output)


if __name__ == "__main__":
    unittest.main()
