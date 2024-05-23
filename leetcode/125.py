"""
    File: 125.py
    Title: Valid Palindrome
    Difficulty: Easy
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1

        def valid(c):
            return "a" <= c <= "z" or "A" <= c <= "Z" or "0" <= c <= "9"

        while lo < hi:
            while lo < len(s) and not valid(s[lo]):
                lo += 1
            while hi > 0 and not valid(s[hi]):
                hi -= 1
            if lo >= len(s) or hi < 0:
                break
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1
        return True
