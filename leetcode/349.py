"""
    File: 349.py
    Title: Intersection of Two Arrays
    Difficulty: Easy
    URL: https://leetcode.com/problems/intersection-of-two-arrays/
"""

import unittest

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        # Output
        output = [2]

        solution = Solution()
        self.assertEqual(solution.intersection(nums1, nums2), output)

    def test_example2(self):
        # Input
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        # Output
        output = [9, 4]

        solution = Solution()
        self.assertEqual(solution.intersection(nums1, nums2), output)


if __name__ == "__main__":
    unittest.main()
