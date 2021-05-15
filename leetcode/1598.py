"""
    File: 1598.py
    Title: Crawler Log Folder
    Difficulty: Easy
    URL: https://leetcode.com/problems/crawler-log-folder/
"""

import unittest

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations = 0
        for log in logs:
            if log == "../":
                if operations > 0:
                    operations -= 1
            elif log == "./":
                continue
            else:
                operations += 1
        return operations


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        logs = ["d1/", "d2/", "../", "d21/", "./"]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.minOperations(logs), output)

    def test_example2(self):
        # Input
        logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.minOperations(logs), output)

    def test_example1(self):
        # Input
        logs = ["d1/", "../", "../", "../"]
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.minOperations(logs), output)


if __name__ == "__main__":
    unittest.main()
