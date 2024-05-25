"""
    File: 66.py
    Title: Plus One
    Difficulty: Easy
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        for i in range(len(digits) - 1, -1, -1):
            if carry:
                n = digits[i] + 1
                if n == 10:
                    digits[i] = 0
                    carry = True
                else:
                    digits[i] = n
                    carry = False
            else:
                break
        if carry:
            return [1] + digits
        return digits
