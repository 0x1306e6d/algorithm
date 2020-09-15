"""
    File: 334.py
    Title: Increasing Triplet Subsequence
    Difficulty: Medium
    URL: https://leetcode.com/problems/increasing-triplet-subsequence/
"""

import unittest

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = None
        second = None

        for i, n in enumerate(nums):
            if first is None:
                first = n
            else:
                if second is None:
                    if first < n:
                        second = n
                    else:
                        first = n
                else:
                    if second < n:
                        return True
                    else:
                        if first < n:
                            second = n
                        else:
                            first = n
        return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 2, 3, 4, 5]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.increasingTriplet(nums), output)

    def test_example2(self):
        # Input
        nums = [5, 4, 3, 2, 1]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.increasingTriplet(nums), output)


if __name__ == "__main__":
    unittest.main()
