"""
    File: 239.py
    Title: Sliding Window Maximum
    Difficulty: Hard
    URL: https://leetcode.com/problems/sliding-window-maximum/
"""

import unittest

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_windows = []
        last_max_window = None
        for i in range(len(nums) - k + 1):
            if last_max_window is None or nums[i - 1] == last_max_window:
                last_max_window = max(nums[i:i + k])
            else:
                last_max_window = max(last_max_window, nums[i + k - 1])
            max_windows.append(last_max_window)
        return max_windows


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        # Output
        output = [3, 3, 5, 5, 6, 7]

        solution = Solution()
        self.assertEqual(solution.maxSlidingWindow(nums, k), output)


if __name__ == "__main__":
    unittest.main()
