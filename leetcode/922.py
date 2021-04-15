"""
    File: 922.py
    Title: Sort Array By Parity II
    Difficulty: Easy
    URL: https://leetcode.com/problems/sort-array-by-parity-ii/
"""

import unittest

from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        ans = []
        for e, o in zip(even, odd):
            ans.append(e)
            ans.append(o)
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [4, 2, 5, 7]
        # Output
        output = [4, 5, 2, 7]

        solution = Solution()
        self.assertEqual(solution.sortArrayByParityII(nums), output)

    def test_example2(self):
        # Input
        nums = [2, 3]
        # Output
        output = [2, 3]

        solution = Solution()
        self.assertEqual(solution.sortArrayByParityII(nums), output)


if __name__ == "__main__":
    unittest.main()
