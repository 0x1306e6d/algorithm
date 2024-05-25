"""
    File: 202.py
    Title: Happy Number
    Difficulty: Easy
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        while n not in memo:
            memo.add(n)

            happy = 0
            i = n
            while i:
                d = i % 10
                happy += d * d
                i //= 10

            if happy == 1:
                return True
            n = happy
        return False
