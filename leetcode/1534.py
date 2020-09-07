"""
    File: 1534.py
    Title: Count Good Triplets
    Difficulty: Easy
    URL: https://leetcode.com/problems/count-good-triplets/
"""

import unittest

from typing import List


class Solution:
    def countGoodTriplets(self,
                          arr: List[int],
                          a: int,
                          b: int,
                          c: int) -> int:
        length = len(arr)
        count = 0
        for i in range(length):
            for j in range(i + 1, length):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, length):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    if abs(arr[i] - arr[k]) > c:
                        continue
                    count += 1
        return count


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        arr = [3, 0, 1, 1, 9, 7]
        a = 7
        b = 2
        c = 3
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.countGoodTriplets(arr, a, b, c), output)

    def test_example2(self):
        # Input
        arr = [1, 1, 2, 2, 3]
        a = 0
        b = 0
        c = 1
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.countGoodTriplets(arr, a, b, c), output)


if __name__ == "__main__":
    unittest.main()
