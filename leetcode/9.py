"""
    File: 9.py
    Title: Palindrome Number
    Difficulty: Easy
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        base = 1
        while x // base >= 10:
            base *= 10

        ltr = rtl = x
        while ltr and rtl:
            a = ltr // base
            b = rtl % 10
            if a != b:
                return False
            ltr = ltr % base
            rtl = rtl // 10
            base = base // 10
        return True
