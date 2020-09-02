"""
    File: 1342.py
    Title: Number of Steps to Reduce a Number to Zero
    Difficulty: Easy
    URL: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""

import unittest


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        n = num
        while n > 0:
            if (n % 2) == 0:
                n //= 2
            else:
                n -= 1
            count += 1
        return count


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        num = 14
        # Output
        output = 6

        solution = Solution()
        self.assertEqual(solution.numberOfSteps(num), output)

    def test_example2(self):
        # Input
        num = 8
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.numberOfSteps(num), output)

    def test_example3(self):
        # Input
        num = 123
        # Output
        output = 12

        solution = Solution()
        self.assertEqual(solution.numberOfSteps(num), output)


if __name__ == "__main__":
    unittest.main()
