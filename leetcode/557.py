"""
    File: 557.py
    Title: Reverse Words in a String III
    Difficulty: Easy
    URL: https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        stack = []
        for c in s:
            if c == " ":
                while stack:
                    ans += stack.pop()
                ans += " "
            else:
                stack.append(c)
        while stack:
            ans += stack.pop()
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "Let's take LeetCode contest"
        # Output
        output = "s'teL ekat edoCteeL tsetnoc"

        solution = Solution()
        self.assertEqual(solution.reverseWords(s), output)

    def test_example2(self):
        # Input
        s = "God Ding"
        # Output
        output = "doG gniD"

        solution = Solution()
        self.assertEqual(solution.reverseWords(s), output)


if __name__ == "__main__":
    unittest.main()
