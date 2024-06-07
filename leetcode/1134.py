"""
    File: 1134.py
    Title: Armstrong Number
    Difficulty: Easy
"""


class Solution:
    def isArmstrong(self, n: int) -> bool:
        target = n
        digits = []
        while n:
            digits.append(n % 10)
            n = n // 10
        power = 0
        for digit in digits:
            power += digit ** len(digits)
        return target == power
