"""
    File: 680.py
    Title: Valid Palindrome II
    Difficulty: Easy
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(i, j, delete):
            if i >= j:
                return True
            if s[i] == s[j]:
                return palindrome(i + 1, j - 1, delete)
            elif delete:
                return False
            return palindrome(i + 1, j, True) or palindrome(i, j - 1, True)

        return palindrome(0, len(s) - 1, False)
