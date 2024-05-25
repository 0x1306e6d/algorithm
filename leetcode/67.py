"""
    File: 67.py
    Title: Add Binary
    Difficulty: Easy
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(map(int, a))
        b = list(map(int, b))
        i, j = len(a) - 1, len(b) - 1
        ans = ""
        carry = 0
        while i >= 0 or j >= 0:
            n = m = 0
            if i >= 0:
                n = a[i]
            if j >= 0:
                m = b[j]
            add = carry + n + m
            if add == 0:
                ans = "0" + ans
            elif add == 1:
                carry = 0
                ans = "1" + ans
            elif add == 2:
                carry = 1
                ans = "0" + ans
            elif add == 3:
                carry = 1
                ans = "1" + ans
            i -= 1
            j -= 1
        if carry:
            ans = "1" + ans
        return ans
