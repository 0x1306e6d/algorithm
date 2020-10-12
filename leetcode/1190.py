"""
    File: 1190.py
    Title: Reverse Substrings Between Each Pair of Parentheses
    Difficulty: Medium
    URL: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
"""

import unittest

from typing import List


class Reversor:
    def __init__(self, parent: 'Reversor' = None):
        self.parent = parent
        self.children = []

    def __repr__(self):
        return "({})".format(self.children)

    def add(self, child) -> None:
        self.children.append(child)

    def flatten(self) -> List[str]:
        flattened = []
        for child in reversed(self.children):
            if type(child) == Reversor:
                flattened += list(reversed(child.flatten()))
            else:
                flattened.append(child)
        return flattened


class Solution:
    def reverseParentheses(self, s: str) -> str:
        root = Reversor()
        current = root
        for c in s:
            if c == '(':
                child = Reversor(current)
                current.add(child)
                current = child
                pass
            elif c == ')':
                current = current.parent
            else:
                current.add(c)
        return "".join(list(reversed(root.flatten())))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "(abcd)"
        # Output
        output = "dcba"

        solution = Solution()
        self.assertEqual(solution.reverseParentheses(s), output)

    def test_example2(self):
        # Input
        s = "(u(love)i)"
        # Output
        output = "iloveu"

        solution = Solution()
        self.assertEqual(solution.reverseParentheses(s), output)

    def test_example3(self):
        # Input
        s = "(ed(et(oc))el)"
        # Output
        output = "leetcode"

        solution = Solution()
        self.assertEqual(solution.reverseParentheses(s), output)

    def test_example4(self):
        # Input
        s = "a(bcdefghijkl(mno)p)q"
        # Output
        output = "apmnolkjihgfedcbq"

        solution = Solution()
        self.assertEqual(solution.reverseParentheses(s), output)


if __name__ == "__main__":
    unittest.main()
