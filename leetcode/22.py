"""
    File: 22.py
    Title: Generate Parentheses
    Difficulty: Medium
    URL: https://leetcode.com/problems/generate-parentheses/
"""

import unittest

from typing import Any, List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(o: int, c: int, s: str) -> List[int]:
            if o + c == 0:
                return [s]

            children = []
            if o > 0:
                children += generate(o - 1, c, s + "(")
            if o < c:
                children += generate(o, c - 1, s + ")")
            return children

        return generate(n, n, "")


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 3
        # Output
        output = ["((()))", "(()())", "(())()", "()(())", "()()()"]

        solution = Solution()
        self.assertListEqualInAnyOrder(solution.generateParenthesis(n), output)

    def test_example2(self):
        # Input
        n = 1
        # Output
        output = ["()"]

        solution = Solution()
        self.assertListEqualInAnyOrder(solution.generateParenthesis(n), output)

    def assertListEqualInAnyOrder(self, a: List[Any], b: List[Any]) -> bool:
        if len(a) != len(b):
            self.fail()

        for p in a:
            if p not in b:
                self.fail()


if __name__ == "__main__":
    unittest.main()
