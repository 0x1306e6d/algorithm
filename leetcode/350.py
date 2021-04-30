"""
    File: 350.py
    Title: Intersection of Two Arrays II
    Difficulty: Easy
    URL: https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

import unittest

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = [0] * 1001
        for n in nums1:
            counts1[n] += 1

        ans = []
        for n in nums2:
            if counts1[n] > 0:
                ans.append(n)
                counts1[n] -= 1
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        # Output
        output = [2, 2]

        solution = Solution()
        self.assertEqual(solution.intersect(nums1, nums2), output)

    def test_example2(self):
        # Input
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        # Output
        output = [9, 4]

        solution = Solution()
        self.assertEqual(solution.intersect(nums1, nums2), output)


if __name__ == "__main__":
    unittest.main()
