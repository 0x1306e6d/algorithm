"""
    File: 1726.py
    Title: Tuple with Same Product
    Difficulty: Medium
    URL: https://leetcode.com/problems/tuple-with-same-product/
"""

import unittest

from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                if product not in products:
                    products[product] = []
                products[product].append((nums[i], nums[j]))

        ans = 0
        for i in products:
            length = len(products[i])
            if length >= 2:
                ans += (((length * (length - 1)) // 2) * 8)
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [2, 3, 4, 6]
        # Output
        output = 8

        solution = Solution()
        self.assertEqual(solution.tupleSameProduct(nums), output)

    def test_example2(self):
        # Input
        nums = [1, 2, 4, 5, 10]
        # Output
        output = 16

        solution = Solution()
        self.assertEqual(solution.tupleSameProduct(nums), output)

    def test_example3(self):
        # Input
        nums = [2, 3, 4, 6, 8, 12]
        # Output
        output = 40

        solution = Solution()
        self.assertEqual(solution.tupleSameProduct(nums), output)

    def test_example4(self):
        # Input
        nums = [2, 3, 5, 7]
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.tupleSameProduct(nums), output)


if __name__ == "__main__":
    unittest.main()
