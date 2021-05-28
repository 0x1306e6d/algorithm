"""
    File: 917.py
    Title: Reverse Only Letters
    Difficulty: Easy
    URL: https://leetcode.com/problems/reverse-only-letters/
"""

import unittest


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def is_letter(c: str) -> bool:
            return ('a' <= c <= 'z') or ('A' <= c <= 'Z')

        ans = ""
        j = len(s) - 1
        while (j >= 0) and (not is_letter(s[j])):
            j -= 1
        for c in s:
            if is_letter(c):
                ans += s[j]
                j -= 1
                while (j >= 0) and (not is_letter(s[j])):
                    j -= 1
            else:
                ans += c
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "ab-cd"
        # Output
        output = "dc-ba"

        solution = Solution()
        self.assertEqual(solution.reverseOnlyLetters(s), output)

    def test_example2(self):
        # Input
        s = "a-bC-dEf-ghIj"
        # Output
        output = "j-Ih-gfE-dCba"

        solution = Solution()
        self.assertEqual(solution.reverseOnlyLetters(s), output)

    def test_example3(self):
        # Input
        s = "ab-cd"
        # Output
        output = "dc-ba"

        solution = Solution()
        self.assertEqual(solution.reverseOnlyLetters(s), output)


if __name__ == "__main__":
    unittest.main()
