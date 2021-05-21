"""
    File: 46.py
    Title: Permutations
    Difficulty: Medium
    URL: https://leetcode.com/problems/permutations/
"""

import unittest

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def generate(k: int, arr: List[int]):
            if k == 1:
                ans.append(arr.copy())
            else:
                for i in range(k):
                    generate(k - 1, arr)

                    if (k % 2) == 0:
                        arr[i], arr[k - 1] = arr[k - 1], arr[i]
                    else:
                        arr[0], arr[k - 1] = arr[k - 1], arr[0]

        generate(len(nums), nums)

        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 2, 3]
        # Output
        output = [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                  [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        solution = Solution()
        self.assertCountEqual(solution.permute(nums), output)

    def test_example2(self):
        # Input
        nums = [0, 1]
        # Output
        output = [[0, 1], [1, 0]]

        solution = Solution()
        self.assertCountEqual(solution.permute(nums), output)

    def test_example3(self):
        # Input
        nums = [1]
        # Output
        output = [[1]]

        solution = Solution()
        self.assertCountEqual(solution.permute(nums), output)


if __name__ == "__main__":
    unittest.main()
