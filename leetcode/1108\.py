"""
    File: 1108.py
    Title: Defanging an IP Address
    Difficulty: Easy
    URL: https://leetcode.com/problems/defanging-an-ip-address/
"""

import unittest


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        address = "1.1.1.1"
        # Output
        output = "1[.]1[.]1[.]1"

        solution = Solution()
        self.assertEqual(solution.defangIPaddr(address), output)

    def test_example2(self):
        # Input
        address = "255.100.50.0"
        # Output
        output = "255[.]100[.]50[.]0"

        solution = Solution()
        self.assertEqual(solution.defangIPaddr(address), output)


if __name__ == "__main__":
    unittest.main()
